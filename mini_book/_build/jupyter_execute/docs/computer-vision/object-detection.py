#!/usr/bin/env python
# coding: utf-8

# # Mini retinanet object detection pytorch implementation
#  <sub> [Convex Optimization](https://github.com/jmhuer), [Linear Programming](https://github.com/jmhuer),  [General Programming](https://github.com/jmhuer)</sub>
# 
#  **In this blog post I will explain what an SDP is and one application: how to find optimal bridge points using Python libraries: scikit, numpy, pytorch**
# 
# 
# ## Introduction
# 
# An SDP (Semidefinite Programming) is a superclass of LP (linear programming). Its called an SDP because the programs can
# 
# There are many applications such as:
# 
# -   Machine learning and data science
# -   Astronomy
# -   Artificial intelligence
# -   Chemistry
# -   Computational biology
# 
# 
# 
# 
# ## Formal Defenition
# 
# > **Semidefinite Programming (SDP)** has the form
# >
# >```{math}
# >\begin{array}{ll}
# >\operatorname{minimize} & C \bullet X \\
# >\text { s.t. } & A_{i} \bullet X=b_{i} \quad i=1, \ldots, m \\
# >& X \succeq 0
# >\end{array}
# >```
# >```{math}
# >C \bullet X:=\sum_{i=1}^{n} \sum_{j=1}^{n} C_{i j} X_{i j}
# >```
# 
# 
# 
# 
# 
# 
# ## Linear Programming and SDP
# 
# A linear program LP is a special instance of an SDP.
# This means the LP can be written as an SDP
# 
# ```{math}
# \begin{aligned}
# &\operatorname{minimize} \quad C \bullet X\\
# &\begin{array}{ll}
# \text { s.t. } & A_{i} \bullet X=b_{i}\quad i=1, \ldots, m \\
# & X_{i j}=0 \quad i=1, \ldots, n   \quad j=i+1, \ldots, n \\
# & X \succeq 0
# \end{array}
# \end{aligned}
# ```
# 
# 
# ```{math}
# C=\left(\begin{array}{cccc}
# c_{1} & 0 & \ldots & 0 \\
# 0 & c_{2} & \ldots & 0 \\
# \vdots & \vdots & \ddots & \vdots \\
# 0 & 0 & \ldots & c_{n}
# \end{array}\right)
# \quad
# X=\left(\begin{array}{cccc}
# x_{1} & 0 & \ldots & 0 \\
# 0 & x_{2} & \ldots & 0 \\
# \vdots & \vdots & \ddots & \vdots \\
# 0 & 0 & \ldots & x_{n}
# \end{array}\right)
# ```
# 
# 
# ```{math}
# \begin{aligned}
# A_{i}=\left(\begin{array}{cccc}
# a_{i 1} & 0 & \ldots & 0 \\
# 0 & a_{i 2} & \ldots & 0 \\
# \vdots & \vdots & \ddots & \vdots \\
# 0 & 0 & \ldots & a_{i n}
# \end{array}\right) \quad   i=1, \ldots, m
# \end{aligned}
# ```
# 
# 
# 
# 
# 
# 
# ## Numerical Example
