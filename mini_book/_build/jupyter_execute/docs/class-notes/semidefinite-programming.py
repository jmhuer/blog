#!/usr/bin/env python
# coding: utf-8

# # Deep learning
# 
#  <sub> [Computer Vision](https://github.com/jmhuer)</sub>
# 
#  **In this blog post we will compare Frank Wolfe vs ProjGD to solve a contrained optimization problem**
# 
# 
# ## Introduction
# 
# The Frank Wolfe algorithm can be defined as:
# 
# ***
# **Projected Gradient Algorithm**
# ***
# 1. Chose initial $x_0$
# 
# 2. For next step: $x^{(k)}=P_{C}\left(x^{(k-1)}-t_{k} \nabla f\left(x^{(k-1)}\right)\right)$
# 
# ***
# 
# ## Formal Defenition
