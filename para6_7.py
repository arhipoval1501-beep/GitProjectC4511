import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("Warning, no code her", SyntaxWarning)
warnings.warn("Warning, modulenot import", ImportWarning)

