import requests
from datetime import datetime
from typing import Union
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/socialminer/api/reddit34'

mcp = FastMCP('reddit34')

@mcp.tool()
def popular_posts(sort: Annotated[str, Field(description='you can just send new or hot')],
                  cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Popular Posts'''
    url = 'https://reddit34.p.rapidapi.com/getPopularPosts'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sort': sort,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def top_popular_posts(time: Annotated[str, Field(description='you can just select one item from below: hour day week month year all')],
                      cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Top Popular Posts'''
    url = 'https://reddit34.p.rapidapi.com/getTopPopularPosts'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'time': time,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def rising_popular_posts(cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Rising Popular Posts'''
    url = 'https://reddit34.p.rapidapi.com/getRisingPopularPosts'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def top_posts_by_username(username: Annotated[str, Field(description='')],
                          time: Annotated[str, Field(description='you can just select one item from below: hour day week month year all')],
                          cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Top Posts By Username'''
    url = 'https://reddit34.p.rapidapi.com/getTopPostsByUsername'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'time': time,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def posts_by_subreddit(subreddit: Annotated[str, Field(description='example: reddit.com/r/memes')],
                       sort: Annotated[str, Field(description='you can just select one item from below: new hot rising')],
                       cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Posts By Subreddit'''
    url = 'https://reddit34.p.rapidapi.com/getPostsBySubreddit'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'subreddit': subreddit,
        'sort': sort,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def top_posts_by_subreddit(subreddit: Annotated[str, Field(description='example: reddit.com/r/memes')],
                           time: Annotated[str, Field(description='you can just select one item from below: hour day week month year all')],
                           cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Top Posts By Subreddit'''
    url = 'https://reddit34.p.rapidapi.com/getTopPostsBySubreddit'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'subreddit': subreddit,
        'time': time,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def posts_by_username(username: Annotated[str, Field(description='')],
                      sort: Annotated[str, Field(description='you can just send new or hot')],
                      cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Posts By Username'''
    url = 'https://reddit34.p.rapidapi.com/getPostsByUsername'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'sort': sort,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def post_details(post_url: Annotated[str, Field(description='')]) -> dict: 
    '''Post Details'''
    url = 'https://reddit34.p.rapidapi.com/getPostDetails'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'post_url': post_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def comments_by_username(username: Annotated[str, Field(description='')],
                         sort: Annotated[str, Field(description='you can just send new or hot')],
                         cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Comments By Username'''
    url = 'https://reddit34.p.rapidapi.com/getCommentsByUsername'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'sort': sort,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def top_comments_by_username(username: Annotated[str, Field(description='')],
                             time: Annotated[str, Field(description='you can just select one item from below: hour day week month year all')],
                             cursor: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Top Comments By Username'''
    url = 'https://reddit34.p.rapidapi.com/getTopCommentsByUsername'
    headers = {'x-rapidapi-host': 'reddit34.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'time': time,
        'cursor': cursor,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()



if __name__ == '__main__':
   mcp.run(transport="stdio")
