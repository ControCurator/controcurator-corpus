# ControCurator Controversy Corpus
This corpus contains crowdsourced annotations on controversy aspects, as part of the [ControCurator](http://controcurator.org) project.

## Experimental Setup
We evaluated the controversy aspects through a crowdsourcing experiment using the [CrowdFlower](http://crowdflower.com) platform. The collected annotations from this experiment were evaluated using the [CrowdTruth](http://crowdtruth.org) methodology for measuring the quality of the annotations, the annotators, and the annotated articles. The relevance of each of the aspects was collected by asking the annotators whether they applied to the main topic of a given newspaper article. For this, we used a collection of 5 048 The Guardian articles that were retrieved through the Guardian news API. In order to save cost and focus on the main topic of an article only the first two paragraphs of each article were used. In an initial pilot we used 100 articles to test the use of a five point likert-scale answers versus "yes/no/I don't know" type answers, and additionally whether showing five comments would help annotators identify whether the topic in an article is controversial. In a second pilot we evaluated with the same dataset whether rephrasing of the aspects and adding the time-persistence would make the identification more clear.


## Results
The results of the first pilot showed that for both settings when showing the article comments the number of annotators that select "I don't know" option is significantly smaller (p-value = 0.003). Additionally, we found that the "yes/no/I don't know" setup always finished faster. Although this difference is not significant (p-value = 0.0519), it may indicate that annotators were more willing to perform this task. Based on this we conclude that the variant *with comments and yes-no answers* gave the best performance in terms of speed and annotation quality. The results of the second pilot showed the rephrasing of the questions improved the identification as the number of people that selected the "I don't know" option dropped from 15% to 3% with p=0.0001.

In the main experiment 5048 articles were annotated by 1 659 annotators resulting in 31 888 annotations. The evaluation of the controversy aspects was a two-fold: first the Pearson correlation coefficients were measured in order to identify how strong an aspect correlated with controversy in each judgment. Second, linear regression was applied to learn the regression coefficient between all of the aspects combined and the controversy score for a judgment. This value indicates the weight of an aspect with respect to the other aspects. The emotion aspect of an article was found to be the strongest indicator for controversy using both measures, while the multitude of actors was the weakest. The openness was said to be present most in 70.9% of the annotations, was annotated with a majority in 73% of the articles, and was found to be the most clearly represented aspect.


## Papers
This dataset is built and used for the following papers. Please cite them if you decide to use our work.

Benjamin Timmermans, Lora Aroyo, Tobias Kuhn, Kaspar Beelen, Evangelos Kanoulas, Bob van de Velde, Gerben van Eerten: [ControCurator: Understanding Controversy Using Collective Intelligence](http://data.btimmermans.com/ci2017controcurator.pdf). Collective Intelligence Conference 2017

```
@article{timmermanscontrocuratorci,
  title={ControCurator: Human-Machine Framework For Identifying Controversy},
  author={Timmermans, Benjamin and Beelen, Kaspar and Aroyo, Lora and Kanoulas, Evangelos and Kuhn, Tobias and van de Velde, Bob and van Eerten, Gerben},
  journal={Collective Intelligence Conference},
  year={2017}
}
```

Benjamin Timmermans, Kaspar Beelen, Lora Aroyo, Evangelos Kanoulas, Tobias Kuhn, Bob van de Velde, Gerben van Eerten: [ControCurator: Human-Machine Framework For Identifying Controversy](http://data.btimmermans.com/ictopen2017controcurator.pdf). ICT Open 2017

```
@article{timmermanscontrocuratorictopen,
  title={ControCurator: Understanding Controversy Using Collective Intelligence},
  author={Timmermans, B and Aroyo, L and Kuhn, T and Beelen, K and Kanoulas, E and van de Velde, B},
  journal={ICT Open},
  year={2017}
}
```