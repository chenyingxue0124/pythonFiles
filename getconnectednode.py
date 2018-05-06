import queue
import sys

def get_connected_node(word):
    Dict = {"AA":1,
            "BB":2,
            "AB":3,
            "AAAA":4}
    returnDict = {}
    k = " "

    for i in range(len(word)):
        for j in range(1,len(word)+1):
            if word[i:j] in Dict:
                k = word[:i]+word[j:]
                returnDict.update({k:Dict[word[i:j]]})
    return returnDict
        

print(get_connected_node("AABBAA"))

def calculate_distance(word,dict):
    que = queue.Queue()
    # score_dict: Dictionay, {string, [score,parent_string]}
    score_dict = {word:[0, ""]}
    que.put(word)
    while not que.empty():
        #calculate all the connected node
    
    
if __name__ =="__main__":
    terminal_input=sys.argv[1:]
    print(terminal_input)