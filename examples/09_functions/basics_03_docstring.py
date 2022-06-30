# source https://github.com/carlmontanari/scrapli/blob/master/scrapli/helper.py#L171

def ttp_parse(template, output):
    """
    Parse output with TTP, try to return structured output
    Args:
        template: TextIOWrapper or string path to template to use to parse data
        output: unstructured output from device to parse
    Returns:
        output: structured data
    Raises:
        N/A
    """
