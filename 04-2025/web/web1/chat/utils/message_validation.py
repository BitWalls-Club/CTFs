import re

BLACKLISTED_TAGS = [
    "a2", "abbr", "acronym", "address", "animate", "animatemotion", "animatetransform", "applet", "area", "article",
    "aside", "audio", "audio2", "b", "bdi", "bdo", "big", "blink", "blockquote", "body", "br", "button", "canvas",
    "caption", "center", "cite", "code", "col", "colgroup", "command", "content", "data", "datalist", "dd", "del",
    "details", "dfn", "dialog", "dir", "div", "dl", "dt", "element", "em", "embed", "fieldset", "figcaption", "figure",
    "font", "footer", "form", "frame", "frameset", "h1", "head", "header", "hgroup", "hr", "html", "i", "iframe",
    "iframe2", "image", "image2", "image3", "img", "img2", "input", "input2", "input3", "input4", "ins", "kbd", "keygen",
    "label", "legend", "li", "link", "listing", "main", "map", "mark", "marquee", "menu", "menuitem", "meta", "meter",
    "multicol", "nav", "nextid", "nobr", "noembed", "noframes", "noscript", "object", "ol", "optgroup", "option",
    "output", "p", "param", "picture", "plaintext", "pre", "progress", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp",
    "script", "section", "select", "set", "shadow", "slot", "small", "source", "spacer", "span", "strike", "strong",
    "sub", "summary", "sup", "svg", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time",
    "title", "tr", "track", "tt", "u", "ul", "var", "video", "video2", "wbr", "xmp"
]

tag_regex = re.compile(r"<\s*(" + "|".join(BLACKLISTED_TAGS) + r")\b", re.IGNORECASE)

EXTRA_PATTERNS = [
    re.compile(r"<script", re.IGNORECASE),
    re.compile(r"\{\{.*?\}\}"), 
    re.compile(r"javascript:", re.IGNORECASE),
    re.compile(r"<iframe", re.IGNORECASE),
    re.compile(r"<img", re.IGNORECASE),
]

def is_safe_message(message: str) -> bool:
    """Returns False if message contains any unsafe content."""
    if tag_regex.search(message):
        return False
    for pattern in EXTRA_PATTERNS:
        if pattern.search(message):
            return False
    return True
