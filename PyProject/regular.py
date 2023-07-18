import re
def domain_name(url):
    reexp = "(//|\.)"
    if re.split(reexp, url)[0] in ["http:", "https:"]:
        if re.split(reexp, url)[2] == "www":
            result = re.split(reexp, url)[4]
        else:
            result = re.split(reexp, url)[2]
    else:
        result = re.split(reexp, url)[0]
    if re.split(reexp, url)[0] == "www":
        result = re.split(reexp, url)[2]
    return result 
