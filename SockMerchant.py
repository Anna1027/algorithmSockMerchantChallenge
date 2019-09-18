ar = [1,1,2,2,3,3,3,2,4,5,4,5]

def sockMerchant(n, ar):
  sock_count={}
  pairs = 0
  for i in ar:
    sock_count[i]=sock_count.get(i,0)+1
    if sock_count[i]==2:
      pairs+=1
      sock_count[i]=0
  return pairs

print(sockMerchant(1, ar))
