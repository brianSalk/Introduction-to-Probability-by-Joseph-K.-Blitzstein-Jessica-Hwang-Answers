# Introduction-to-Probability-by-Joseph-K.-Blitzstein-Jessica-Hwang-Answers
My answers for problems at the end of each chapter in the book Introduction to Probability by Joseph K. Blitzstein, Jessica Hwang 

## Chapter 2
**Question 11** 
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
A. Find P (A), the true proportion of people who voted for A.<summary>Question</summary></details>

<details>$P(A)=\frac{9}{23}$<summary>Answer</summary></details>


<details><summary>Explaination</summary> We are given the following: <br> $P(W|A) = .7$ <br> $P(W|A^c) = .3$ and <br>$60\%$ of people surveyed voted for candidate $A$ <br>
so for this we use Bayes theorem, plug in our values and then solve for $P(A)$, which is different than the previous problems.  <br>
$P(A|W) = \dfrac{P(W|A)\cdot P(A)}{P(W|A)P(A) + P(W|A^C)(1-P(A))}$ <br> 
  now plug in values for your variables, remembering that $P(A|W) = .6$, we get <br>
  $.6 = \dfrac{.7 \cdot P(A)}{.7P(A) + .3(1-P(A))}$<br>
After algebraically solving for $P(A)$, we get our final answer of $P(A) = \frac{9}{23}$</details>
