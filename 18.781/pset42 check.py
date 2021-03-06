
def check_mod(stop,j, p):
    for i in xrange(1, stop):
        print (i**(i+j) + j**(i+j)) % p, ((i+j)**(i+j) % p)

def check_power(stop, j, p):
    for i in xrange(1, stop):
        print i**j % p, (2*p+i)**j % p

def create_sequence(stop, mod):
    seq = []
    for i in xrange(1, stop):
        seq.append(i**i % mod)
    return seq

def get_min_period(seq):
    current_seq = []
    i = 0
    counter = 0
    while i < len(seq):
        if (len(current_seq) > 0 and seq[i] == current_seq[counter]):
            counter += 1
            if counter == len(current_seq):
                return current_seq
        current_seq.append(seq[i])
        i += 1
    return False

if __name__ == '__main__':
    check_power(20,3,5)

