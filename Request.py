from google_play_scraper import app, Sort, reviews_all

import pandas as pd
import numpy as np
import json, os, uuid

g_reviews = reviews_all(
        "com.google.android.apps.fitness",
        sleep_milliseconds=0, # defaults to 0
        lang='es', # defaults to 'en'
        country='CL', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    )
g_df = pd.DataFrame(np.array(g_reviews),columns=['review'])
g_df2 = g_df.join(pd.DataFrame(g_df.pop('review').tolist()))

g_df2.drop(columns={'userImage', 'reviewCreatedVersion', 'userName'},inplace = True)
g_df2.rename(columns= {'score': 'rating', 'reviewId': 'review_id', 'content': 'review_description', 'at': 'review_date', 'replyContent': 'developer_response', 'repliedAt': 'developer_response_date', 'thumbsUpCount': 'thumbs_up'},inplace = True)
g_df2.insert(loc=0, column='source', value='Google Play')
g_df2.insert(loc=3, column='review_title', value=None)
g_df2['laguage_code'] = 'es'
g_df2['country_code'] = 'CL'
g_df2.to_csv('D:/App request/Datos_GfitH.csv')
