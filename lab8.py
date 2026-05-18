import sys

def sort_by_length(words):
    buckets = [[] for _ in range(51)]
    for word in words:
        buckets[len(word)].append(word)
    
    sorted_words = []
    for bucket in buckets:
        for word in bucket:
            sorted_words.append(word)
    return sorted_words


def get_max_chain(words):
    words = sort_by_length(words)
    
    dp = {}
    max_len = 0
    
    for word in words:
        best_prev = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in dp:
                best_prev = max(best_prev, dp[prev] + 1)
        
        dp[word] = best_prev
        max_len = max(max_len, best_prev)
        
    return max_len

def main():
    try:
        with open('wchain.in', 'r') as f:
            lines = f.read().splitlines()
        
        if not lines: return
        
        n = int(lines[0])
        words = lines[1:n+1]
        
        result = get_max_chain(words)
        
        with open('wchain.out', 'w') as f:
            f.write(str(result))
            
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    main()
