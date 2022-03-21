import sys
from scipy import stats

descriptions = ["\t1) Binomial --> number of successes in n trials",
    "\t2) Negative Binomial --> number of trials to produce n successes",
    "\t3) Poisson --> number of successes occurring in a time period",
    "\t4) Exponential",
    "\t5) Normal",
    "\t6) Chi-Square",
    "\t7) t",
    "\t8) F",
    "\t9) Uniform Distribution",
    "\t10) Exit"]

def quit():
    print("Exiting program...")
    sys.exit()

def get_choice(maximum):
    choice = 0
    while choice not in range(1, maximum+1):
        print("Input choice: ", end="")
        try:
            choice = input()
            if choice == "exit":
                quit()
            choice = int(choice)
        except Exception as e:
            print(e)
            choice = 0
    print()
    return choice

def get_values(*args):
    while True:
        values = input().split()

        if len(values) == 1 and values[0] == "exit":
            quit()

        if len(values) != len(args):
            continue

        try:
            results = []
            for i in range(len(values)):
                value = args[i](values[i])
                results.append(value)
            return results
        except Exception as e:
            print(e)

def binomial():
    print("X ~ B(n, p) where\n\tX = number of successes\n\tn = number of trials\n\tp = probability of success")
    print("Select the probability:")
    print("1) P(X <= k) or P(X = k) or P(X > k)")
    print("2) P(X <= x) >= p'")
    print("3) E(X) or V(X)")
    
    choice = get_choice(3)
    if choice == 1:
        while True:
            try:
                print("Enter n, p, and k:")
                n, p, k = get_values(int, float, int)
                result = stats.binom.cdf(k,n,p)
                print("P(X <= ", k, ") = ", result, sep="")
                result = stats.binom.pmf(k,n,p)
                print("P(X = ", k, ") = ", result, sep="")
                result = 1 -stats.binom.cdf(k,n,p)
                print("P(X > ", k, ") = ", result, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 2:
        while True:
            try:
                print("Enter n, p, and p':")
                n, p, pp = get_values(int, float, float)
                result = stats.binom.ppf(pp,n,p)
                print("P(X < ", result, ") >= ", pp, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 3:
        while True:
            try:
                print("Enter n and p:")
                n, p= get_values(int, float)
                result = n*p
                print("E(X) = np = ", result, sep="")
                result = n*p*(1-p)
                print("V(X) = np(1-p) = ", result, sep="")
                return
            except Exception as e:
                print(e)

def negative_binomial():
    print("X ~ NB(n, p) where\n\tX = number of trials\n\tn = number of successes\n\tp = probability of success")
    print("Select the probability:")
    print("1) P(X <= k) or P(X = k) or P(X > k)")
    print("2) P(X <= x) >= p'")
    print("3) E(X) or V(X)")
    
    choice = get_choice(3)
    if choice == 1:
        while True:
            try:
                print("Enter n, p, and k:")
                n, p, k = get_values(int, float, int)
                result = stats.nbinom.cdf(k-n,n,p)
                print("P(X <= ", k, ") = ", result, sep="")
                result = stats.nbinom.pmf(k-n,n,p)
                print("P(X = ", k, ") = ", result, sep="")
                result = 1 -stats.nbinom.cdf(k-n,n,p)
                print("P(X > ", k, ") = ", result, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 2:
        while True:
            try:
                print("Enter n, p, and p':")
                n, p, pp = get_values(int, float, float)
                result = stats.binom.ppf(pp,n,p) + n
                print("P(X <= ", result, ") >= ", pp, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 3:
        while True:
            try:
                print("Enter n and p:")
                n, p= get_values(int, float)
                result = n/p
                print("E(X) = np = ", result, sep="")
                result = n*(1-p)/(p**2)
                print("V(X) = np(1-p) = ", result, sep="")
                return
            except Exception as e:
                print(e)

def poisson():
    print("X ~ P(avg) where\n\tX = number of success occurring during a time interval\n\tavg = average number of successes in a time interval")
    print("Select the probability:")
    print("1) P(X <= k) or P(X = k) or P(X > k)")
    print("2) P(X <= x) >= p'")
    print("3) E(X) or V(X)")
    
    choice = get_choice(3)
    if choice == 1:
        while True:
            try:
                print("Enter avg and k:")
                avg, k = get_values(float, int)
                result = stats.poisson.cdf(k,avg)
                print("P(X <= ", k, ") = ", result, sep="")
                result = stats.poisson.pmf(k,avg)
                print("P(X = ", k, ") = ", result, sep="")
                result = 1 - stats.poisson.cdf(k,avg)
                print("P(X > ", k, ") = ", result, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 2:
        while True:
            try:
                print("Enter avg and p':")
                avg, pp = get_values(float, float)
                result = stats.poisson.ppf(pp,avg)
                print("P(X <= ", result, ") >= ", pp, sep="")
                return result
            except Exception as e:
                print(e)
    if choice == 3:
        while True:
            try:
                print("Enter avg:")
                avg = get_values(float)[0]
                print("E(X) = V(X) = ", avg, sep="")
                return avg
            except Exception as e:
                print(e)

def exponential():
    print("X ~ Exp(1/avg) where\n\tavg = E(X)")
    print("Select the probability:")
    print("1) P(X <= k) or P(X = k) or P(X > k)")
    print("2) P(X <= x) = p'")
    
    choice = get_choice(2)
    if choice == 1:
        while True:
            try:
                print("Enter avg and k:")
                avg, k = get_values(float, int)
                result = stats.expon.cdf(k,0,avg)
                print("P(X <= ", k, ") = ", result, sep="")
                result = stats.expon.pdf(k,0,avg)
                print("P(X = ", k, ") = ", result, sep="")
                result = 1 - stats.expon.cdf(k,0,avg)
                print("P(X > ", k, ") = ", result, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 2:
        while True:
            try:
                print("Enter avg and p':")
                avg, pp = get_values(float, float)
                result = stats.expon.ppf(pp,0,avg)
                print("P(X <= ", result, ") = ", pp, sep="")
                return
            except Exception as e:
                print(e)

def normal():
    print("X ~ N(mew, sigma^2) where\n\tmew = E(X)\n\tsigma^2 = V(X)")
    print("Select the probability:")
    print("1) P(X <= k) or P(X = k) or P(X > k)")
    print("2) P(X <= x) = p'")
    print("3) P(Z >= z) = p'")
    
    choice = get_choice(3)
    if choice == 1:
        while True:
            try:
                print("Enter E(X), standard deviation, and k:")
                e, sd, k = get_values(float, float, float)
                result = stats.norm.cdf(k,e,sd)
                print("P(X <= ", k, ") = ", result, sep="")
                result = stats.norm.pdf(k,e,sd)
                print("P(X = ", k, ") = ", result, sep="")
                result = 1 - stats.norm.cdf(k,e,sd)
                print("P(X > ", k, ") = ", result, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 2:
        while True:
            try:
                print("Enter E(X), standard deviation, and p':")
                e, sd, pp = get_values(float, float, float)
                result = stats.norm.ppf(pp,e,sd)
                print("P(X < ", result, ") = ", pp, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 3:
        while True:
            try:
                print("Enter p':")
                pp = get_values(float)
                result = stats.norm.ppf(pp,0,1)
                print("P(Z >= ", result, ") = ", pp, sep="")
                return
            except Exception as e:
                print(e)

def chi_square():
    print("X ~ chisq(n) where\n\tn = degrees of freedom")
    print("Select the probability:")
    print("1) P(X <= k) or P(X = k) or P(X > k)")
    print("2) P(X <= x) = p' or P(X >= x) = p'")
    
    choice = get_choice(2)
    if choice == 1:
        while True:
            try:
                print("Enter n and k:")
                n, k = get_values(int, float)
                result = stats.chi2.cdf(k,n)
                print("P(X <= ", k, ") = ", result, sep="")
                result = stats.chi2.pmf(k,n)
                print("P(X = ", k, ") = ", result, sep="")
                result = 1 - stats.chi2.cdf(k,n)
                print("P(X > ", k, ") = ", result, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 2:
        while True:
            try:
                print("Enter n and p':")
                n, pp = get_values(int, float)
                result = stats.chi2.ppf(pp,n)
                print("P(X <= ", result, ") = ", pp, sep="")
                result = stats.chi2.ppf(1-pp,n)
                print("P(X >= ", result, ") = ", pp, sep="")
                return
            except Exception as e:
                print(e)

def t():
    print("X ~ t(n) where\n\tn = degrees of freedom")
    print("Select the probability:")
    print("1) P(X <= k) or P(X = k) or P(X > k)")
    print("2) P(X <= x) = p' or P(X >= x) = p'")
    
    choice = get_choice(2)
    if choice == 1:
        while True:
            try:
                print("Enter n and k:")
                n, k = get_values(int, float)
                result = stats.t.cdf(k,n)
                print("P(X <= ", k, ") = ", result, sep="")
                result = stats.t.pmf(k,n)
                print("P(X = ", k, ") = ", result, sep="")
                result = 1 - stats.t.cdf(k,n)
                print("P(X > ", k, ") = ", result, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 2:
        while True:
            try:
                print("Enter n and p':")
                n, pp = get_values(int, float)
                result = stats.t.ppf(pp,n)
                print("P(X <= ", result, ") = ", pp, sep="")
                result = stats.t.ppf(1-pp,n)
                print("P(X >= ", result, ") = ", pp, sep="")
                return
            except Exception as e:
                print(e)

def F():
    print("X ~ F(n) where\n\tn = degrees of freedom")
    print("Select the probability:")
    print("1) P(X <= k) or P(X = k) or P(X > k)")
    print("2) P(X <= x) = p' or P(X >= x) = p'")
    
    choice = get_choice(2)
    if choice == 1:
        while True:
            try:
                print("Enter n and k:")
                n, k = get_values(int, float)
                result = stats.f.cdf(k,n)
                print("P(X <= ", k, ") = ", result, sep="")
                result = stats.f.pmf(k,n)
                print("P(X = ", k, ") = ", result, sep="")
                result = 1 - stats.f.cdf(k,n)
                print("P(X > ", k, ") = ", result, sep="")
                return
            except Exception as e:
                print(e)
    if choice == 2:
        while True:
            try:
                print("Enter n and p':")
                n, pp = get_values(int, float)
                result = stats.f.ppf(pp,n)
                print("P(X <= ", result, ") = ", pp, sep="")
                result = stats.f.ppf(1-pp,n)
                print("P(X >= ", result, ") = ", pp, sep="")
                return
            except Exception as e:
                print(e)

def uniform():
    print("X is uniformly distributed on the interval [a, b]")
    while True:
        try:
            print("Enter a and b:")
            a, b = get_values(float, float)
            print("f(x) =", 1/(b-a))
            print("E(X) =", (a+b)/2)
            print("V(X) =", (b-a)**2/12)
            return
        except Exception as e:
            print(e)

while True:
    print("\nSelect the distribution:")
    for description in descriptions:
        print(description)
    
    choice = get_choice(len(descriptions))
    if choice == len(descriptions):
        break
    functions = [None, binomial, negative_binomial, poisson, exponential, normal, chi_square, t, F, uniform]
    functions[choice]()
