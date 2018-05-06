import queue
import sys
import time

def get_connected_node(word, wordDict):
    returnDict = {}
    for i in range(len(word)):
        for j in range(1, len(word) + 1):
            if word[i:j] in wordDict:
                returnDict.update({word[:i] + word[j:]: [wordDict[word[i:j]], i, word[i:j]]})
    return returnDict

def dfsprint(wordDict, score_dict, now_word,word, output_stack):
    if word == now_word:
        while output_stack:
            obj = output_stack.pop()
            print(obj[0],obj[1])
        return 0
    output_stack.append([score_dict[now_word][2],score_dict[now_word][3]])
    dfsprint(wordDict,score_dict,score_dict[now_word][1],word, output_stack)
    return 0

def calculate_distance(word, dict):
    minValue=["", 0] #最小值的初始化
    que = queue.Queue()  #初始化一个队列
    #score_dict: Dictionay, {string, [score, parent_string, index]}
    score_dict = {word: [0, "", 0]}
    # offer s in Q
    que.put(word)
    qset=set([word])
    while not que.empty():
        # u:= poll Q
        node=que.get()
        qset.remove(node)
        #for each edge (u,v) in E(G)
        connectedNode=get_connected_node(node, dict)
        for eachnode in connectedNode:
            #if d(u) + w(u,v) < d(v)
            index=connectedNode[eachnode][1]
            dictindex=connectedNode[eachnode][2]
            du_p_wuv=score_dict[node][0]+connectedNode[eachnode][0]
            if eachnode in score_dict:
                # Relaxation Succeed
                if du_p_wuv < score_dict[eachnode][0]:
                    if du_p_wuv < minValue[1]:
                        minValue = [eachnode, du_p_wuv]
                       #print("minValue:", du_p_wuv)
                    score_dict.update({eachnode:[du_p_wuv, node, index,dictindex]})
                    if eachnode not in qset:
                        qset.add(eachnode)
                        que.put(eachnode)
            else:
                # Relaxation Succeed
                if du_p_wuv < minValue[1]:
                    minValue=[eachnode, du_p_wuv]
                    #print("minValue:", du_p_wuv)
                score_dict.update({eachnode: [du_p_wuv, node, index,dictindex]})
                if eachnode not in qset:
                    qset.add(eachnode)
                    que.put(eachnode)
                # calculate all the connected node
                
    output_stack = []
    dfsprint(dict, score_dict, minValue[0],word,output_stack)
    return -minValue[1]

if __name__ == "__main__":
    word = "AABBAABBAA"
    wordDict = {"AA":-1,
                "BB":-2,
                "AB":-3,
                "AAAA":-12}
    print(calculate_distance(word,wordDict))