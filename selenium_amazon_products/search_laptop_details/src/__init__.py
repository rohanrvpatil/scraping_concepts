from .config import SEARCH_URL
from .config import config_driver

from .scraping import (
    preprocess_title,preprocess_about_this_item, preprocess_technical_details_summary,safe_extract,
    scrape_page, get_next_page
    )