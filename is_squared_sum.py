class Sol:
    def is_squared_sum(self,n):
        num=n
        for i in range(2,num+1):
            count=0
            if num%i==0:
                while num%i==0:
                    count+=1
                    if num/i!=1:
                        num=num/i
                    else:
                        break
                if num%4==3 and count%2!=0:
                    return False
        return True

if __name__ == '__main__':
    p=Sol()
    print(p.is_squared_sum(19))
