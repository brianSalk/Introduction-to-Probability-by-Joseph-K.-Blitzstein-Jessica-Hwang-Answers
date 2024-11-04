# Introduction-to-Probability-by-Joseph-K.-Blitzstein-Jessica-Hwang-Answers
My answers for problems at the end of each chapter in the book Introduction to Probability by Joseph K. Blitzstein, Jessica Hwang 

## Chapter 2
### Question 1
<details>A spam filter is designed by looking at commonly occurring phrases in spam. Suppose
that 80% of email is spam. In 10% of the spam emails, the phrase “free money” is used,
whereas this phrase is only used in 1% of non-spam emails. A new email has just arrived,
which does mention “free money”. What is the probability that it is spam?<summary>Question</summary></details>

<details><summary>Answer</summary></details>

<details><summary>Explaination</summary></details>

### Question 3
<details>According to the CDC (Centers for Disease Control and Prevention), men who smoke are
23 times more likely to develop lung cancer than men who don’t smoke, Also according
to the CDC, 21.6% of men in the U.S. smoke, What is the probability that a man in
the U.S. is a smoker, given that he develops lung cancer?
<summary>Question</summary></details>

<details>$P(S|C)=\dfrac{\frac{23}{24} \cdot .216}{.239\overline{6}}\approx.864$<summary>Answer</summary></details>

<details>$S=is\_smoker$<br>$C=has\_cancer$<br>$P(S)=.216$<br>$P(C|S)=23/24$<br>
  $P(S|C)=\dfrac{P(C|S)P(S)}{P(C)}$<br>$P(C) = P(C|S)P(S) + P(C|S^c)P(S^c)$<br>plugging in our values from above, we get<br>
  $P(C) = \frac{23}{24}\cdot .216 + \frac{1}{24} \cdot .784 = .239\overline{6}$<br>our final equation is<br>
  $P(S|C)=\dfrac{23/24 \cdot .216}{.239\overline{6}}\approx.864$<br>
  Notice that we do not actually know what the rate of cancer is.  Knowing that smokers are 23 times more likely to get cancer is enough for us to answer this question.<summary>Explaination</summary></details>

### Question 4
<details>Fred is answering a multiple-choice problem on an exam, and has to choose one of n
options (exactly one of which is correct). Let K be the event that he knows the answer,
and R be the event that he gets the problem right (either through knowledge or through
Conditional probability 75
luck). Suppose that if he knows the right answer he will definitely get the problem right,
but if he does not know then he will guess completely randomly. Let P(K) = p.<br><br>
(a) Find P(K|R) (in terms of p and n).<br>
(b) Show that P(K|R) ≥ p, and explain why this makes sense intuitively. When (if ever)
does P(K|R) equal p?<summary>Question</summary></details>

### Question 11
<details>An exit poll in an election is a survey taken of voters just after they have voted. One
major use of exit polls has been so that news organizations can try to figure out as
soon as possible who won the election, before the votes are officially counted. This has
been notoriously inaccurate in various elections, sometimes because of selection bias:
the sample of people who are invited to and agree to participate in the survey may not
be similar enough to the overall population of voters.
Consider an election with two candidates, Candidate A and Candidate B. Every voter
is invited to participate in an exit poll, where they are asked whom they voted for; some
accept and some refuse. For a randomly selected voter, let A be the event that they voted
for A, and W be the event that they are willing to participate in the exit poll. Suppose
that P (W |A) = 0.7 but P (W |Ac) = 0.3. In the exit poll, 60% of the respondents say
they voted for A (assume that they are all honest), suggesting a comfortable victory for
A. Find P(A), the true proportion of people who voted for A.<summary>Question</summary></details>

<details>$P(A)=\frac{9}{23}$<summary>Answer</summary></details>


<details><summary>Explaination</summary> We are given the following: <br> $P(W|A) = .7$ <br> $P(W|A^c) = .3$ and <br>$60\%$ of people surveyed voted for candidate $A$ <br>
so for this we use Bayes theorem, plug in our values and then solve for $P(A)$, which is different than the previous problems.  <br>
$P(A|W) = \dfrac{P(W|A)\cdot P(A)}{P(W|A)P(A) + P(W|A^C)(1-P(A))}$ <br> 
  now plug in values for your variables, remembering that $P(A|W) = .6$, we get <br>
  $.6 = \dfrac{.7 \cdot P(A)}{.7P(A) + .3(1-P(A))}$<br>
After algebraically solving for $P(A)$, we get our final answer of $P(A) = \frac{9}{23}$</details>
