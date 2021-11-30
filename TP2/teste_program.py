def verify_req(requests):
    
    #Verify current state of requests
    states = {}
    offset = 0 
    for case, user_id in requests:
        states[user_id] = None if case == "done" else offset
        offset += 1
    #Store only requests on going
    requests = [ (states[key], key) for key in states.keys() if states[key] ]
    requests.sort(key=lambda x: x[0])

    return requests




if __name__ == "__main__":
    requests = [
        ['request', 'Pub-Vinicius'], ['request', 'Pub-Vinicius2'], 
        ['request', 'Pub-Vinicius3'], ['request', 'Pub-Vinicius4'], 
        ['request', 'Pub-Vinicius3'], ['request', 'Pub-Vinicius5'], 
        ['done', 'Pub-Vinicius'], ['done', 'Pub-Vinicius2'],
        ['done', 'Pub-Vinicius2'], ['request', 'Pub-Vinicius2'],
        ['request', 'Pub-Vinicius'], ['done', 'Pub-Vinicius5'],
        ['done', 'Pub-Vinicius3'], ['done', 'Pub-Vinicius2'], 
        ['request', 'Pub-Vinicius3'] ]
    

    r = verify_req(requests)
    print(r)