from dataclasses import dataclass, field
from typing import List, Dict, Optional, Union

@dataclass
class Value:
    name: str
    lifeSpan: int
    ttl: Optional[int] = None
    params: Optional[Dict[str, str]] = None

@dataclass
class Context:
    values: List[Value]

@dataclass
class SimpleText:
    text: str

@dataclass
class SimpleImage:
    imageUrl: str
    altText: str

@dataclass
class Button:
    action: str
    label: str
    webLinkUrl: Optional[str] = None
    messageText: Optional[str] = None
    phoneNumber: Optional[str] = None
    blockId: Optional[str] = None
    extra: Optional[Dict[str, str]] = None

@dataclass
class TextCard:
    title: str
    description: str
    buttons: List[Button]

@dataclass
class Thumbnail:
    imageUrl: str

@dataclass
class BasicCard:
    title: str
    description: str
    thumbnail: Thumbnail
    buttons: List[Button]

@dataclass
class CommerceCardThumbnail:
    imageUrl: str
    description : str
    price : 
    link: Dict[str, str]

@dataclass
class CommerceCardProfile:
    imageUrl: str
    nickname: str

@dataclass
class CommerceCard:
    title: str
    description: str
    price: int
    discount: int
    currency: str
    thumbnails: List[CommerceCardThumbnail]
    profile: CommerceCardProfile
    buttons: List[Button]

@dataclass
class Item:
    title: str
    description: str
    imageUrl: Optional[str] = None
    link: Optional[Dict[str, str]] = None
    action: Optional[str] = None
    blockId: Optional[str] = None
    messageText: Optional[str] = None
    extra: Optional[Dict[str, str]] = None

@dataclass
class ListCardHeader:
    title: str

@dataclass
class ListCard:
    header: ListCardHeader
    items: List[Item]
    buttons: List[Button]

@dataclass
class ItemListSummary:
    title: str
    description: str

@dataclass
class ItemCardProfile:
    title: str
    imageUrl: str

@dataclass
class ItemCard:
    imageTitle: Optional[Item] = None
    title: Optional[str] = None
    description: Optional[str] = None
    thumbnail: Optional[Thumbnail] = None
    profile: Optional[ItemCardProfile] = None
    itemList: Optional[List[Item]] = None
    itemListAlignment: Optional[str] = None
    itemListSummary: Optional[ItemListSummary] = None
    buttons: Optional[List[Button]] = None
    buttonLayout: Optional[str] = None

@dataclass
class CarouselItem:
    title: str
    description: str
    thumbnail: Thumbnail
    buttons: List[Button]

@dataclass
class CarouselHeader:
    title: str
    description: str
    thumbnail: Thumbnail

@dataclass
class Carousel:
    type: str
    items: List[Union[CarouselItem, ListCard]]
    header: Optional[CarouselHeader] = None

@dataclass
class Template:
    outputs: List[Union[SimpleText, SimpleImage, TextCard, BasicCard, CommerceCard, ListCard, ItemCard, Carousel]]
    quickReplies: Optional[List[QuickReplies]] = None

@dataclass
class JsonStructure:
    version: str = "2.0"
    context: Optional[Context] = None
    template: Optional[Template] = None
    data: Optional[Dict[str, str]] = None
