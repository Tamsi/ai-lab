# RL Post-Training for LLMs

**Status:** Not started  
**Milestone:** LLMs + RL  
**Related exercise:** [rl_policy_gradient_cartpole](../../exercises/pytorch/rl_policy_gradient_cartpole/)  
**Papers:** [2606.18089](../../papers/llms/2026-compositional-generalization-sft-rl.md)

## Intuition

After SFT, **reinforcement learning** adjusts the model to maximize a **reward**
(correctness, human preference, task score). The policy is the language model;
actions are tokens; the environment is the partial sequence being generated.

Common variants: **RLHF** (reward model from human prefs), **PPO**, **GRPO**, **DPO** (preference optimization without explicit RL loop).

## Formal definition

Maximize expected reward:

\[
J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)]
\]

Policy gradient (schematic):

\[
\nabla_\theta J \approx \mathbb{E}\left[ \sum_t \nabla_\theta \log \pi_\theta(a_t|s_t) \cdot A_t \right]
\]

where \(A_t\) is an advantage estimate.

## Why it matters in machine learning

- Aligns LLM outputs with goals SFT cannot specify as demonstrations alone
- In [2606.18089](../../papers/llms/2026-compositional-generalization-sft-rl.md): RL **decomposes** SFT traces into reusable modules

## Minimal implementation

Start with tabular or CartPole policy gradient before token-level PPO.

## Experiment

Train a tiny policy on CartPole with REINFORCE; relate to token-level credit assignment.

## Connection to research papers

Asymmetric role vs SFT in compositional generalization.

## What I still do not understand

- Credit assignment over long reasoning chains
- KL penalty to reference model — why and how much
- Difference between PPO, GRPO, and DPO in practice
