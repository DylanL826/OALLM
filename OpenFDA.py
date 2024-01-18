import requests

"""Test function to make requests to OpenFDA api."""
def OpenFDA_request():
    # Search fields: 
    #   patient.drug.activesubstance.activesubstancename
    #   
    req_parameters = {'search':'patient.reaction.reactionmeddrapt:"Weight increased"',
                      'limit':'500'}
    res = requests.get('https://api.fda.gov/drug/event.json', params=req_parameters)
    print(res.status_code)
    print(res.url)
    #print(res.json())
    res_json_obj = res.json()
    # patient_obj = res_json_obj['results'][0]['patient']
    # drug_list = patient_obj['drug']
    # reaction_list = patient_obj['reaction']
    # medDRA_terms = list(map(lambda obj: obj['patient']['reaction'][0]['reactionmeddrapt'], res_json_obj['results']))
    
    # Create matrix of medDRA terms from the returned patient records.
    medDRA_terms = []
    for patient in res_json_obj['results']:
        # Get list of reactions for each patient.
        cur_pt_rct_ls = list(map(lambda reaction: reaction['reactionmeddrapt'], patient['patient']['reaction']))
        medDRA_terms.append(cur_pt_rct_ls)
        print(cur_pt_rct_ls)
    #print(medDRA_terms)
    print("END")

if __name__ == '__main__':
    OpenFDA_request()