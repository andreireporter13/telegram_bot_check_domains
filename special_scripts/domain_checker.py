# Domain checker script 
# 
# 
import whois
# 
# 
# 
def info_whois(domain_name: str) -> dict: 
    """
    This general function return dict with info about any domain
    """
    flags = 0
    flags = flags 

    domain_info = whois.whois(domain_name, flags=True)

    return domain_info   


def cr_date(domain_name: str) -> str: 
    """
        This domain return a creation_date.
    """
    domain_info = info_whois(domain_name)

    return f'Domain that you inserted was created on ->{domain_info.creation_date}<-'


def exp_date(domain_name: str) -> str:
    """
        This domain return a expiration_date.
    """
    domain_info = info_whois(domain_name)

    return f'Domain that you inserted will be expired on ->{domain_info.expiration_date}<-'
    

def domain_register(domain_name: str) -> str: 
    """
        This domain return updated_time.
    """
    domain_info = info_whois(domain_name)

    return f'Domain that you inserted is in register ->{domain_info.registrar}<-'


def n_servers(domain_name: str) -> str: 
    """
        This function return a name_servers.
    """
    domain_info = info_whois(domain_name)

    return f'The name servers are ->{domain_info.name_servers}<-'

