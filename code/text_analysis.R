# Loading packages
library(tidyverse)
library(tidytext)
library(SnowballC)
library(wordcloud)
library(udpipe)
library(lattice)

# Loading the raw text data from data > clean_data folder
raw_data <- read.csv(paste(getwd(),"/data/clean_data/final_dataset_textanalysis.csv",sep = ""))

# Selecting only english story texts and campaigns with stories
raw_data <- raw_data[raw_data['language'] == "en",]

# Selecting the story texts
story_texts_data = select(raw_data, Story_Original, CampaignURL)

tidy_storytext = unnest_tokens(story_texts_data, word, Story_Original)

# Stop word removal

data("stop_words")
tidy_storytext2 = tidy_storytext %>% 
  anti_join(stop_words)

patterndigits = '\\b[0-9]+\\b'

tidy_storytext2$word = tidy_storytext2$word %>%
  str_remove_all(patterndigits)

tidy_storytext2$word = tidy_storytext2$word %>%
  str_replace_all('[:space:]', '')

tidy_storytext3 = tidy_storytext2 %>% 
  filter(!(word == ''))

tidy_storytext4 = tidy_storytext3 %>%
  mutate_at("word", funs(wordStem((.), language="en")))