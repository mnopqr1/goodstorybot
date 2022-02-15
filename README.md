# goodstorybot
a bot generating really good stories, and tweeting them

One day, a friend sent me a link to a [wonderfully weird list of sentences](https://github.com/daanzu/speech-training-recorder/blob/master/prompts/timit.txt) that were originally used as prompts for the [TIMIT acoustic speech corpus](https://www.nist.gov/publications/darpa-timit-acoustic-phonetic-continuous-speech-corpus-cd-rom-timit).

I was curious to see how the latest open source text generation would react to these seemingly random sentences. A Colab notebook made available by the EleutherAI collective made this incredibly simple.

Then, during [National Novel Generation Month](https://nanogenmo.github.io/), I wrote the part of the bot that [tweets](https://twitter.com/goodstorybot) a random choice of one of its really good stories every day. 

This repository contains the notebook used to generate the stories and the script used to tweet them.