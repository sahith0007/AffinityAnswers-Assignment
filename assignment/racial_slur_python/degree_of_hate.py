#Function to analyse the tweets in the file
def degree_of_hate(file):
    #Set of words that indicate racial slurs
    hate_words = ["black","kill","protest","etc"]
    with open(file) as tweets:
        for tweet in tweets:
            count = 0
            #To exclude the empty lines in the file
            if tweet.strip():
                #Spliting the tweet into lower case words for easy comparision
                for word in tweet.lower().split():
                    #For identifying user name
                    if "@" in word:
                        user = word
                    #Checking whether the tweet consists of racial slurs
                    if "#" in word:
                        word = word.replace("#",'')
                    if word in hate_words:
                        count += 1 
                #Calculating the degree of profanity for user tweet
                if count <= 3:
                    print("{}-Normal".format(user))
                elif count <= 10:
                    print("{}-Moderate".format(user))
                else:
                    print("{}-High".format(user))

degree_of_hate("demo.txt")