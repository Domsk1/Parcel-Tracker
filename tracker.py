import json
import sched
import time
from datetime import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from os import path
import requests
import jsondiff
import setup


""" TODO better customization
Add support for multiple parcels at once
add support specifically for 'customs' 'problem'
don't say its a update when youre searching for a new parcel"""

SLUGS = ["ems-china", "dhl"]  # Repfam I hear you


class SlugException(Exception):

    """Exception class for Slug exceptions"""

    def __init__(self, m):
        self.message = m

    def __str__(self):
        return self.message


class TrackingNotifier:

    """Class to track a parcel and notify on status changes

    Uses endpoint ``https://api.aftership.com/v4``

    Args:
        api_key (str): API_KEY for the endpoint
    kwargs:
        slugs: Slugs to append to the supported slugs, for example 'china-ems'
        base_url: change the endpoint
        file: change the filename to save the latest status JSON to
    """

    def __init__(self, api_key, **kwargs):
        """Initializes the TrackingNotifier instance and checks for kwargs for configuration"""
        self.__API_KEY = api_key

        if "BASE_URL" in kwargs:
            self.__BASE_URL = kwargs["BASE_URL"]
        else:
            self.__BASE_URL = "https://api.aftership.com/v4"

        if "slugs" in kwargs:
            SLUGS.extend(kwargs["slugs"])

        self.__file = "tracking.png"

        if "lang" in kwargs:
            self.__lang = kwargs["lang"]
        else:
            self.__lang = "None"

        if "notify_check_interval" in kwargs:
            self.__notify_check_interval = kwargs["notify_check_interval"]
        else:
            self.__notify_check_interval = 30

        self.__HEADER = {"aftership-api-key": api_key, "Content-Type": "application/json"}

        self.tracking_number = None
        self.slug = None
        self.__mail = {}
        self.__mail['From'] = "hotellarcher@gmail.com"
        self.__mail['Password'] = "Larcher2018"
        self.__mail['Subject'] = "Your parcel status has been updated!"

    def track(self, tracking_number, slug, **kwargs):
        """Get the latest track information for a parcel as a JSON object

        Args:
            tracking_number (str): The tracking number of the parcel you are trying to track
            slug (str): The parcel service shipping your parcel
            req_params (dict): Additional parameters for the GET request
        Returns:
            a JSON object of the newest tracking information for the given shipment
        Examples:
            track('EA3251CN', 'china-ems', lang='en')
        """
        self.tracking_number = tracking_number
        self.slug = slug
        self.__file = path.join(path.dirname(__file__), tracking_number + ".json")

        if kwargs:
            self.params = kwargs

        if slug not in SLUGS:
            raise SlugException("Error: Slug '{}' is not supported!".format(slug))

        uri = "{}/trackings/{}/{}".format(self.__BASE_URL, slug, tracking_number)

        res = requests.get(uri, params=self.params, headers=self.__HEADER)

        if res.status_code != 200:
            raise Exception("Error: {}".format(res.json()["meta"]["message"]))

        self.__update_file(res.json())

        return res.json(), 200

    def __send_mail(self, message):
        """Sends an email to a specified user

        Args:
            message (str): The message contents
        """
        try:
            msg = MIMEMultipart()
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)  # TODO make others than gmail possible
            server.starttls()
            server.login(self.__mail['From'], password)
            server.sendmail(self.__mail['From'], self.__mail['To'], message.as_string())
            server.quit()

            return "Successfully sent email to {}:".format(self.__mail['To'])
        except:
            return "Error: Could not send email to {}".format(self.__mail['To'])

    def __update_file(self, new):
        """Checks for differences in the tracking file and the new response

        Alerts the user if .continous_notify was called previously

        Args:
            new (JSON): The newest tracking request response
        """
        try:
            with open(self.__file, "r") as f:
                old = json.load(f)

            diff = jsondiff.diff(old, new)
            last_location = self.__get_last_location(new)

            if not last_location:
                return "{}: Parcel tracking is empty".format(dt.now().strftime("%H:%M:%S"))

            if diff:
                self.__write_file(new)  # Update file contents

                msg = "{}: Tracking status updated!\nNew location: {}".format(self.tracking_number, last_location)

                if 'To' in self.__mail:  # Send email if user specified
                    self.__send_mail(msg)
            else:  # Ambiguous else but used for simplicity
                msg = "{}: Updated without change\n{}".format(self.tracking_number, last_location)

            print(msg)
            return msg
        except:
            self.__write_file(new)  # If file doesn't exist it will be created here

    def __write_file(self, new):
        """Overwrites the newest tracking information into the file"""
        with open(self.__file, "w") as f:
            json.dump(new, f, indent=4)

    def __get_last_location(self, track, sort_by="checkpoint_time", date_format="%Y-%m-%dT%H:%M:%S"):
        """Gets information about the latest location of the users parcel

        Args:
            track (JSON): The newest tracking request response
            sort_by (str): The dict key to sort the timeline by. 'checkpoint_time' by default
            date_format (str): The date format used in the JSON response
        Returns:
            a string with the latest location of the parcel
        """
        try:
            checkpoints = track["data"]["tracking"]["checkpoints"]

            # If checkpoints is empty
            if not checkpoints:
                return None

            # Sorts by date and gets the newest element
            last = sorted(checkpoints, key=lambda x: dt.strptime(x[sort_by], date_format), reverse=True)[0]
            return "{}: {} ({})".format(dt.strptime(last[sort_by], date_format).strftime("%d. %b %H:%M:%S"), last["message"], last["location"])
        except:
            print("An error occured trying to get the last parcel location.")
            return None


class MultiTracker():

    """Class for tracking multiple parcels

    Args:
        config (dict): The JSON object of the user config
    """

    def __init__(self, config):
        self.__config = config
        self.__parcels = config["parcels"]
        self.__api = config["api_key"]
        self.__notify_check_interval = 30

    def __track_all(self, sc):
        """Helper method. Loops through every parcel with a delay and updates the parcels tracking"""
        for parcel in self.__parcels:
            notifier = TrackingNotifier(self.__api)
            notifier.track(parcel["tracking_number"], parcel["slug"], lang=config["lang"])
        print("-------------------------------------")
        sc.enter(self.__notify_check_interval, 1, self.__track_all, (sc,))

    def track(self, timeout=None):
        """Start tracking all the parcels in the config"""
        if timeout:
            self.__notify_check_interval = timeout

        s = sched.scheduler(time.time, time.sleep)
        print("Starting tracking in '{}' with status notifications to {}...".format(
            self.__config["lang"], self.__config["email"]))
        print("Checking status {} parcels every {} seconds.\n".format(
            len(self.__parcels), self.__notify_check_interval))
        print("Cancel with CTRL+C ...\n")
        s.enter(0, 1, self.__track_all, (s,))
        s.run()


def read_config(file):
    """Read user configuration from file or create basic config if it doesn't exist"""
    try:
        with open(file, "r") as f:
            content = json.load(f)
        return content
    except:
        setup.setup_config()
        print("Error: Please configure the config file now or start the setup if it is your first time.")


def read_slugs(file):
    """Read slugs from file or create basic slugs if it doesn't exist"""
    try:
        with open(file, "r") as f:
            content = json.load(f)
        return content
    except:
        setup.setup_slugs()
        print("Error: Please add slugs manually or set up the project again!")


if __name__ == "__main__":
    # If run.bat doesn't exist create it (Makes starting the program easier)
    if not path.exists(path.join(path.dirname(__file__), "run.bat")):
        setup.bat()

    config = read_config(path.join(path.dirname(__file__), "config.json"))
    SLUGS.extend(read_slugs(path.join(path.dirname(__file__), "slugs.json")))

    try:
        # Ignore this ugly ass test to see if the config gives key errors LOL
        parcels = config["parcels"]
        config["api_key"]
        config["email"]
        config["lang"]
        # --------------------------------------------
    except Exception as e:
        print("Error reading config! {}".format(e))
        exit()

    try:  # Config seems to be ok
        print("Successfully read user config and supporting {} parcel services".format(len(SLUGS)))
        mt = MultiTracker(config)
        mt.track(30)
    except Exception as e:
        print("Error tracking parcel! {}".format(e))
