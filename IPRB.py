def dominant_allele_probability(k, m, n):
   """
   Calculate the probability that two randomly selected mating organisms will produce an individual 
   possessing a dominant allele based on the frequencies of different genotypes in the population.

   Parameters:
   - k: Number of homozygous dominant individuals.
   - m: Number of heterozygous individuals.
   - n: Number of homozygous recessive individuals.

   Returns:
   - Probability that the offspring will have a dominant allele.

   Explanation:
   The function uses the provided counts of homozygous dominant (k), heterozygous (m), and homozygous 
   recessive (n) individuals to calculate the probability (P(K)) based on the given genotype frequencies. 
   The formula accounts for all possible mating combinations and their probabilities.

   Formula:
   P(K) = (m * (0.5 * m + n + k - 0.75) + k * (n + t - 1)) / (t * (t - 1))

   where t = k + m + n (total population).
   """
   t = k+m+n
   return (m * (0.75 * m + n + k - 0.75) + k * (n + t - 1)) / (t * (t - 1))

n_D, n_H, n_R = map(int, input().split())
print(dominant_allele_probability(n_D, n_H, n_R))
