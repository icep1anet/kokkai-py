import dataclasses
from typing import Literal


@dataclasses.dataclass
class KokkaiSpeech:
    speechID: str
    issueID: str
    imageKind: Literal["会議録", "目次", "索引", "附録", "追録"]
    searchObject: int
    session: int
    nameOfHouse: Literal["参議院", "衆議院", "両院", "両院協議会"]
    nameOfMeeting: str
    issue: str
    date: str
    closing: bool
    speechOrder: int
    speaker: str
    speakerYomi: str
    speakerGroup: str
    speakerPosition: str
    speakerRole: str
    speech: str
    startPage: int
    speechURL: str
    meetingURL: str
    pdfURL: str


@dataclasses.dataclass
class KokkaiSpeechResponse:
    numberOfRecords: int
    numberOfReturn: int
    startRecord: int
    nextRecordPosition: int
    speechRecord: list[KokkaiSpeech]
    
    def __post_init__(self):
        self.speechRecord = [KokkaiSpeech(**record) for record in self.speechRecord]


@dataclasses.dataclass
class KokkaiMeetingSpeech:
    speechID: str
    speechOrder: int
    speaker: str
    speakerYomi: str
    speakerGroup: str
    speakerPosition: str
    speakerRole: str
    speech: str
    startPage: int
    createTime: str
    updateTime: str
    speechURL: str


@dataclasses.dataclass
class KokkaiMeeting:
    issueID: str
    imageKind: Literal["会議録", "目次", "索引", "附録", "追録"]
    searchObject: int
    session: int
    nameOfHouse: Literal["参議院", "衆議院", "両院", "両院協議会"]
    nameOfMeeting: str
    issue: str
    date: str
    closing: bool
    speechRecord: list[KokkaiMeetingSpeech]
    meetingURL: str
    pdfURL: str
    
    def __post_init__(self):
        self.speechRecord = [KokkaiMeetingSpeech(**record) for record in self.speechRecord]


@dataclasses.dataclass
class KokkaiMeetingResponse:
    numberOfRecords: int
    numberOfReturn: int
    startRecord: int
    nextRecordPosition: int
    meetingRecord: list[KokkaiMeeting]
    
    def __post_init__(self):
        self.meetingRecord = [KokkaiMeeting(**record) for record in self.meetingRecord]
