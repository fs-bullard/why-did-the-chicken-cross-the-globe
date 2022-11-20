
install.packages("plotly")

library(plotly)


plot_ly(
  data = Food_emissions,
  x = ~Entity,
  y = ~Emissions.per.kilogram,
  type = "scatter",
  mode = "markers"
)

-----
packages = c('treemap', 'tidyverse')

for(p in packages){library
  if(!require(p, character.only = T)){
    install.packages(p)
  }
  library(p, character.only = T)
}

treemap(Food_emissions,
        index=c("Entity", "Emissions.per.kilogram"),
        vSize="Emissions.per.kilogram",
        vColor="Emissions.per.kilogram",
        title="Emissions per kilogram",
        title.legend = "Emission"
)

----
  library(tidyverse)
library(knitr)
library(plotly)
library(readxl)
library(scales)

Food_emissions %>% kable

Food_emissions <- Food_emissions

plot_ly(data = Food_emissions, x = "Entity", y = "Emissions.per.kilogram", type = "bar", text = "entity", textposition = "auto") %>% 
  layout(title = "Emssions interactive",
         #titlefont = list(size = 28, color = "orange", family = "Calibri"),
         yaxis = list(title = "Emissions",
                      titlefont = list(color = "black", family = "Arial", size = 26),
                      tickfont = list(color = "black", family = "Arial", size = 20)),
         xaxis = list(title = "Entity",
                      titlefont = list(color = "red", family = "Times New Roman", size = 22),
                      tickfont = list(color = "green", family = "Cambria", size = 18)))%>% 
  layout(margin = list( 
    l = 10,
    r = 10,
    b = 0,
    t = 40)) # Use the layout(margin) function to adjust the margins of the graph
-----
packages = c('treemap', 'tidyverse')

for(p in packages){library
  if(!require(p, character.only = T)){
    install.packages(p)
  }
  library(p, character.only = T)
}

treemap(Food_footprints,
        index=c("Entity", "Emissions.per.kilogram"),
        vSize="Emissions.per.kilogram",
        vColor="Emissions.per.kilogram",
        title="Emissions per kilogram",
        title.legend = "Emission"
)

----
  library(plotly)

Recipes <- c("Vegetable lasagne")
red.peppers <- c(0.53)
aubergines <- c(0.53)
olive.oil <- c(0.53)
lasgne.sheets <- c(1.57
)


data <- data.frame(Recipes, red.peppers, aubergines, olive.oil, lasgne.sheets
                   
)

fig <- plot_ly(data, x = ~Recipes, y = ~red.peppers, type = 'bar', name = 'red peppers')
fig <- fig %>% add_trace(y = ~aubergines, name = 'aubergines')
fig <- fig %>% add_trace(y = ~olive.oil, name = 'olive.oil')
fig <- fig %>% add_trace(y = ~lasgne.sheets, name = 'lasgne.sheets')
fig <- fig %>% layout(yaxis = list(title = 'Emission score'), barmode = 'stack')

fig
----
  library(plotly)
library (readxl)


x <- (all_data$categories)
y <- (all_data$Emission.per.kilogram)
text <- (all_data$ingredients)
data <- data.frame(x, y, text)

fig <- plot_ly(data, x = ~x, y = ~y, type = 'bar', text = text,
               marker = list(color = 'rgb(158,202,225)',
                             line = list(color = 'rgb(8,48,107)',
                                         width = 1.5)))
fig <- fig %>% layout(title = "title",
                      xaxis = list(title = ""),
                      yaxis = list(title = ""))

fig
---
  library(plotly)
install.packages("tidyverse")
library("tidyverse")

Chicken.pasta.bake<- all_data %>% filter(title == "Chicken pasta bake")
ingredients <- c(all_data$Emission.per.kilogram)
#LA_Zoo <- c(12, 18, 29)
data <- data.frame(Chicken.pasta.bake, ingredients)

fig <- plot_ly(Chicken.pasta.bake, x = ~ingredients, y = ~Emission.per.kilogram, type = 'bar', name = 'ingredients')
fig <- fig %>% add_trace(y = ~Emission.per.kilogram, name = 'Emission')
fig <- fig %>% layout(yaxis = list(title = 'Count'), barmode = 'stack')

fig2 <- all_data %>% group_by(title)
fig2 <- plot_ly(all_data, x=title, y = Emission.per.kilogram, type = 'bar', group_by = title)
fig2


