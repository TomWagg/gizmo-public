import argparse

tags_from_keywords = [
    {
        "Hopkins2015": ["MAGNETIC", "MHD_B_SET_IN_PARAMS", "MHD_NON_IDEAL", "MHD_CONSTRAINED_GRADIENT"],
        "Hopkins2016": ["MHD_CONSTRAINED_GRADIENT"],
        # TODO: etc. etc. add more here
    }
]

def get_citation_tags_from_config(filepath):
    """Retrieve a list of BiBTeX citation tags based on the settings specified in a configuration file.

    Parameters
    ----------
    filepath : `str`
        Path to the configuration file.

    Returns
    -------
    citations : `list`
        List of BiBTeX citation tags that correspond to the settings in the configuration file.
    """

    # check which settings are turned on in the config file
    settings_on = set()
    with open(filepath, 'r') as file:
        # go through each line
        for line in file:
            # find any lines that aren't blank/comments
            if not line.strip().startswith("#") and len(line.strip()) > 0:
                # take just the initial setting name, remove anything after an equals sign
                setting = line.strip().split(" ")[0]
                setting = setting.split("=")[0] if "=" in setting else setting
                settings_on.add(setting)

    # track which tags are relevant based on the settings    
    citation_tags = set()
    for mapper in tags_from_keywords:
        for tag, keywords in mapper.items():
            if len(set(keywords).intersection(settings_on)) > 0:
                citation_tags.add(tag)

    return sorted(list(citation_tags))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get citation tags based on a configuration file.")
    parser.add_argument("--filepath", "-f", required=True,
                        type=str, help="Path to the configuration file.")
    args = parser.parse_args()

    citation_tags = get_citation_tags_from_config(args.filepath)
    acknowledgement = "This work makes use of the GIZMO code \\citep{Hopkins2014, Springel2005}."

    if len(citation_tags) > 0:
        acknowledgement += " GIZMO simulations in this study were run with additional features, which are based on a variety of other works \\citep{" + ", ".join(citation_tags) + "}."

    print(acknowledgement)
