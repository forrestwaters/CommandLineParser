class CliParser(object):
    """
    Command-line parsing utility
    Users must specify a description and help_message
    Allow users to add args that are required
    Accept flags (-h, -r, etc.) as well as options (--help, --verbose, etc.)
    """

    def __init__(self, description, help_message):
        self.description = description
        self.help = help_message
