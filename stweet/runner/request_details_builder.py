"""Utils to prepare data."""
from typing import Dict

from stweet.model.search_tweets_task import SearchTweetsTask
from stweet.runner.search_runner import SearchRunContext

_bearer_token = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4pu' \
                'Ts%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'


def scrap_tweets_get_params(
        search_run_context: SearchRunContext,
        search_tweets_task: SearchTweetsTask
) -> Dict[str, str]:
    """Method to prepare requests params to get tweets."""
    return dict([
        ('include_can_media_tag', '1'),
        ('include_ext_alt_text', 'true'),
        ('include_quote_count', 'true'),
        ('include_reply_count', '1'),
        ('tweet_mode', 'extended'),
        ('include_entities', 'true'),
        ('include_user_entities', 'true'),
        ('include_ext_media_availability', 'true'),
        ('send_error_codes', 'true'),
        ('simple_quoted_tweet', 'true'),
        ('count', 100),
        ('cursor', search_run_context.scroll_token),
        ('spelling_corrections', '1'),
        ('ext', 'mediaStats%2ChighlightedLabel'),
        ('tweet_search_mode', 'live'),
        ('f', 'tweets'),  # if not config.Popular_tweets
        ('q', search_tweets_task.get_full_search_query())
    ])


def scrap_tweets_get_headers(search_run_context: SearchRunContext) -> Dict[str, str]:
    """Method to prepare requests headers to get tweets."""
    return dict([
        ("authorization", _bearer_token),
        ("x-guest-token", search_run_context.guest_auth_token)
    ])