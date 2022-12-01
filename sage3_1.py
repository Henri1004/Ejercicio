
# In[11]:


x = var("x")
solve(x^3 - x == 7*x^2 - 7, x)


# In[21]:


t = var("t")
solve(abs(t - 7) >= 3, t)


# In[26]:


x, y = var('x, y')
solve([2*x+y==17, x-3*y==-16], x, y)


# In[ ]:
