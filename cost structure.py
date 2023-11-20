#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyecharts import options as opts
from pyecharts.charts import Sankey


# In[2]:


colors = [
    "#67001f",
    "#b2182b",
    "#d6604d",
    "#f4a582",
    "#fddbc7",
    "#d1e5f0",
    "#92c5de",
    "#4393c3",
    "#2166ac",
    "#053061",
]


# In[3]:


nodes = [
    {"name": "Cost"},
    {"name": "Cost for Services Providers"},
    #
    {"name": "Operational Expense"},
    {"name": "Prmotional Expense"},
    {"name": "Information Technology Expense"},
    {"name": "Communication Expense"},
    {"name": "Consultancy&Outsourced Services"},
    #
    {"name": "Cost of services"},
    #
    {"name": "Compilance Fee"},
    {"name": "Contingency Expense"},
    #
    {"name": "Derivative"},
    {"name": "Foreign Exchange Expense"},
    {"name": "Fair Value Hedges"},
    {"name": "Cash Flow Hedges"},
    {"name": "Undesignated hedges"},
    #
    {"name": "Agent Commissions Expense"},
    {"name": "Banks Fees"},
    {"name": "Credit losses"},
    {"name": "Depreciation&Amortization"},
    #category
    {"name": "Cost for Customers"},
    {"name": "Company Revenue"},
]


# In[4]:


links = [
    {"source": "Cost", "target": "Cost for Services Providers", "value": 1},
    {"source": "Cost", "target": "Cost for Customers", "value": 1.11},
    {"source": "Cost for Services Providers", "target": "Cost of services", "value": 1.2},
    {"source": "Cost of services", "target": "Agent Commissions Expense", "value": 1.22},
    {"source": "Cost of services", "target": "Operational Expense", "value": 1.222},
    {"source": "Cost for Services Providers", "target": "Compilance Fee", "value": 1.3},
    {"source": "Cost for Services Providers", "target": "Derivative", "value": 1.333},
    {"source": "Agent Commissions Expense", "target": "Banks Fees", "value": 1.33},
    {"source": "Agent Commissions Expense", "target": "Credit losses", "value": 1.1111},
    {"source": "Agent Commissions Expense", "target": "Depreciation&Amortization", "value": 1.111111},
    {"source": "Operational Expense", "target": "Prmotional Expense", "value": 1.21},
    {"source": "Operational Expense", "target": "Information Technology Expense", "value": 1.122},
    {"source": "Operational Expense", "target": "Communication Expense", "value": 1.12},
    {"source": "Operational Expense", "target": "Consultancy&Outsourced Services", "value": 1.112},
    {"source": "Compilance Fee", "target": "Contingency Expense", "value": 1.11112},
    {"source": "Derivative", "target": "Foreign Exchange Expense", "value": 1.1},
    {"source": "Derivative", "target": "Fair Value Hedges", "value": 1},
    {"source": "Derivative", "target": "Cash Flow Hedges", "value": 1},
    {"source": "Derivative", "target": "Undesignated hedges", "value": 1},
    #
    #customer
    {"source": "Cost for Customers", "target": "Company Revenue", "value": 1},
]


# In[5]:


c = (
    Sankey()
    .set_colors(colors)
    .add(
        "sankey",
        nodes=nodes,
        links=links,
        pos_bottom="15%",
        focus_node_adjacency="allEdges",
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.3, color="source"),
        label_opts=opts.LabelOpts(is_show=True, position="left",color="#0A0A0D",font_family="Arial",font_size="10"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title= "Cost Structure"),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
    )
    .render("你好.html")
)


# In[ ]:




