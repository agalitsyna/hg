# generated by datamodel-codegen:
#   filename:  schema.json
#   timestamp: 2022-01-30T17:40:24+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union, Tuple, Literal, Sequence

from pydantic import BaseModel as _BaseModel, Extra, Field, conlist, validator
from .display import renderers

import slugid

# Switch default of `exclude_none` to True
class BaseModel(_BaseModel):
    def __rich_repr__(self):
        return self.__iter__()

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)

    def json(self, exclude_none=True, **kwargs):
        return super().json(exclude_none=exclude_none, **kwargs)


class Data(BaseModel):
    url: Optional[str] = None
    server: Optional[str] = None
    filetype: Optional[str] = None
    type: Optional[str] = None
    tilesetInfo: Optional[Dict[str, Any]] = None
    children: Optional[List] = None
    tiles: Optional[Dict[str, Any]] = None


class GenomePositionSearchBox(BaseModel):
    autocompleteServer: Optional[str] = Field(
        default=None,
        examples=["//higlass.io/api/v1"],
        title="The Autocomplete Server URL",
    )
    autocompleteId: Optional[str] = Field(
        default=None, examples=["OHJakQICQD6gTD7skx4EWA"], title="The Autocomplete ID"
    )
    chromInfoServer: str = Field(
        ..., examples=["//higlass.io/api/v1"], title="The Chrominfo Server URL"
    )
    chromInfoId: str = Field(..., examples=["hg19"], title="The Chromosome Info ID")
    visible: Optional[bool] = Field(False, title="The Visible Schema")


class Layout(BaseModel):
    class Config:
        extra = Extra.forbid

    x: int = Field(..., title="The X Position")
    y: int = Field(..., title="The Y Position")
    w: int = Field(..., title="Width")
    h: int = Field(..., title="Height")
    moved: Optional[bool] = None
    static: Optional[bool] = None


class Options(BaseModel):
    extent: Optional[List] = None
    minWidth: Optional[float] = None
    fill: Optional[str] = None
    fillOpacity: Optional[float] = None
    stroke: Optional[str] = None
    strokeOpacity: Optional[float] = None
    strokeWidth: Optional[float] = None
    strokePos: Optional[Union[str, List[Any]]] = None
    outline: Optional[str] = None
    outlineOpacity: Optional[float] = None
    outlineWidth: Optional[float] = None
    outlinePos: Optional[Union[str, List[Any]]] = None


class Overlay(BaseModel):
    class Config:
        extra = Extra.forbid

    chromInfoPath: Optional[str] = None
    includes: Optional[List] = None
    options: Optional[Options] = None
    type: Optional[str] = None
    uid: Optional[str] = None


# Simplified aliases
Domain = Tuple[int, int]
Slug = str


class AxisSpecificLocks(BaseModel):
    class Config:
        extra = Extra.forbid

    axis: Literal["x", "y"]
    lock: str


EnumTrackType = Literal[
    "multivec",
    "1d-heatmap",
    "line",
    "point",
    "bar",
    "divergent-bar",
    "stacked-interval",
    "gene-annotations",
    "linear-2d-rectangle-domains",
    "chromosome-labels",
    "linear-heatmap",
    "1d-value-interval",
    "2d-annotations",
    "2d-chromosome-annotations",
    "2d-chromosome-grid",
    "2d-chromosome-labels",
    "2d-rectangle-domains",
    "2d-tiles",
    "arrowhead-domains",
    "bedlike",
    "cross-rule",
    "dummy",
    "horizontal-1d-annotations",
    "horizontal-1d-heatmap",
    "horizontal-1d-tiles",
    "horizontal-1d-value-interval",
    "horizontal-2d-rectangle-domains",
    "horizontal-bar",
    "horizontal-chromosome-grid",
    "horizontal-chromosome-labels",
    "horizontal-divergent-bar",
    "horizontal-gene-annotations",
    "horizontal-heatmap",
    "horizontal-line",
    "horizontal-multivec",
    "horizontal-point",
    "horizontal-rule",
    "horizontal-vector-heatmap",
    "image-tiles",
    "left-axis",
    "left-stacked-interval",
    "mapbox-tiles",
    "osm-2d-tile-ids",
    "osm-tiles",
    "raster-tiles",
    "simple-svg",
    "square-markers",
    "top-axis",
    "top-stacked-interval",
    "vertical-1d-annotations",
    "vertical-1d-heatmap",
    "vertical-1d-tiles",
    "vertical-1d-value-interval",
    "vertical-2d-rectangle-domains",
    "vertical-bar",
    "vertical-bedlike",
    "vertical-chromosome-grid",
    "vertical-chromosome-labels",
    "vertical-gene-annotations",
    "vertical-heatmap",
    "vertical-line",
    "vertical-multivec",
    "vertical-point",
    "vertical-rule",
    "vertical-vector-heatmap",
    "viewport-projection-center",
    "viewport-projection-horizontal",
    "viewport-projection-vertical",
]


class EnumTrack(BaseModel):
    class Config:
        extra = Extra.forbid

    type: EnumTrackType
    server: Optional[str] = None
    tilesetUid: Optional[str] = None
    data: Optional[Data] = None
    uid: Optional[str] = None
    chromInfoPath: Optional[str] = None
    fromViewUid: Optional[str] = None
    height: Optional[float] = None
    options: Optional[Dict[str, Any]] = None
    width: Optional[float] = None
    x: Optional[float] = None
    y: Optional[float] = None


class HeatmapTrack(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Literal["heatmap"]
    uid: Optional[str] = None
    data: Optional[Data] = None
    height: Optional[float] = None
    options: Optional[Dict[str, Any]] = None
    position: Optional[str] = None
    server: Optional[str] = None
    tilesetUid: Optional[str] = None
    width: Optional[float] = None
    transforms: Optional[List] = None


class IndependentViewportProjectionTrack(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Literal[
        "viewport-projection-horizontal",
        "viewport-projection-vertical",
        "viewport-projection-center",
    ]
    fromViewUid: None = None
    uid: Optional[str] = None
    projectionXDomain: Optional[Domain] = None
    projectionYDomain: Optional[Domain] = None
    options: Optional[Dict[str, Any]] = None
    transforms: Optional[List] = None
    width: Optional[float] = None
    x: Optional[float] = None
    y: Optional[float] = None


class Lock(BaseModel):
    class Config:
        extra = Extra.allow

    uid: Optional[Slug] = None
    ignoreOffScreenValues: Optional[bool] = None

    def iter_uids(self):
        for key, _ in self:
            if key not in ("uid", "ignoreOffScreenValues"):
                yield key


class LocationLocks(BaseModel):
    class Config:
        extra = Extra.forbid

    locksByViewUid: Dict[str, Union[str, AxisSpecificLocks]] = {}
    locksDict: Dict[str, Lock] = {}


class ValueScaleLocks(BaseModel):
    class Config:
        extra = Extra.forbid

    locksByViewUid: Dict[str, str]
    locksDict: Dict[str, Lock]


class ZoomLocks(BaseModel):
    class Config:
        extra = Extra.forbid

    locksByViewUid: Dict[str, str] = {}
    locksDict: Dict[str, Lock] = {}


class CombinedTrack(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Literal["combined"]
    contents: List["Track"]
    height: Optional[float] = None
    options: Optional[Any] = None
    position: Optional[str] = None
    uid: Optional[str] = None
    width: Optional[float] = None


# Manual entry because not in schema.json
class Tileset(BaseModel):
    class Config:
        extra = Extra.forbid

    tilesetUid: str
    server: str


# Manual entry because not in schema.json
class DividedTrack(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Literal["divided"]
    children: List[Tileset]
    height: Optional[float] = None
    options: Optional[Any] = None
    position: Optional[str] = None
    uid: Optional[str] = None
    width: Optional[float] = None


Track = Union[
    DividedTrack,
    EnumTrack,
    CombinedTrack,
    HeatmapTrack,
    IndependentViewportProjectionTrack,
]


class Viewconf(BaseModel):
    class Config:
        extra = Extra.forbid

    editable: Optional[bool] = True
    viewEditable: Optional[bool] = True
    tracksEditable: Optional[bool] = True
    zoomFixed: Optional[bool] = None
    compactLayout: Optional[bool] = None
    exportViewUrl: Optional[str] = None
    trackSourceServers: Optional[conlist(str, min_items=1)] = None
    zoomLocks: Optional[ZoomLocks] = None
    locationLocks: Optional[LocationLocks] = None
    valueScaleLocks: Optional[ValueScaleLocks] = None
    views: Optional[conlist(View, min_items=1)] = None
    chromInfoPath: Optional[str] = None

    def _repr_mimebundle_(self, include=None, exclude=None):
        renderer = renderers.get()
        return renderer(self.json())

    def display(self):
        """Render top-level chart using IPython.display."""
        from IPython.display import display

        display(self)

    def lock(
        self,
        *locks: Lock,
        zoom: Optional[Union[Sequence[Lock], Lock]] = None,
        location: Optional[Union[Sequence[Lock], Lock]] = None,
    ):
        copy = Viewconf(**self.dict())

        if zoom is None:
            zoom = []
        elif isinstance(zoom, Lock):
            zoom = [zoom]
        else:
            zoom = list(zoom)

        if location is None:
            location = []
        elif isinstance(location, Lock):
            location = [location]
        else:
            location = list(location)

        zoom.extend(locks)
        location.extend(locks)

        if copy.zoomLocks is None:
            copy.zoomLocks = ZoomLocks()

        for lock in zoom:
            assert isinstance(lock.uid, str)
            copy.zoomLocks.locksDict[lock.uid] = lock
            for vuid in lock.iter_uids():
                copy.zoomLocks.locksByViewUid[vuid] = lock.uid

        if copy.locationLocks is None:
            copy.locationLocks = LocationLocks()

        for lock in location:
            assert isinstance(lock.uid, str)
            copy.locationLocks.locksDict[lock.uid] = lock
            for vuid in lock.iter_uids():
                copy.locationLocks.locksByViewUid[vuid] = lock.uid

        return copy


class View(BaseModel):
    class Config:
        extra = Extra.forbid

    layout: Layout
    tracks: Tracks
    uid: Optional[str] = None
    autocompleteSource: Optional[str] = None
    chromInfoPath: Optional[str] = None
    genomePositionSearchBox: Optional[GenomePositionSearchBox] = None
    genomePositionSearchBoxVisible: Optional[bool] = None
    initialXDomain: Optional[Domain] = None
    initialYDomain: Optional[Domain] = None
    overlays: Optional[List[Overlay]] = None
    selectionView: Optional[bool] = None
    zoomFixed: Optional[bool] = None
    zoomLimits: Tuple[float, Optional[float]] = (1, None)

    def __copy_unique__(self):
        copy = View(**self.dict())
        copy.uid = str(slugid.nice())
        return copy

    def domain(
        self,
        x: Optional[Domain] = None,
        y: Optional[Domain] = None,
    ):
        copy = self.__copy_unique__()
        if x is not None:
            copy.initialXDomain = x
        if y is not None:
            copy.initialYDomain = y
        return copy

    # TODO: better name? adjust_layout, resize
    def move(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ):
        copy = self.__copy_unique__()
        if x is not None:
            copy.layout.x = x
        if y is not None:
            copy.layout.y = y
        if width is not None:
            copy.layout.w = width
        if height is not None:
            copy.layout.h = height
        return copy


class Tracks(BaseModel):
    class Config:
        extra = Extra.forbid

    left: Optional[List[Track]] = None
    right: Optional[List[Track]] = None
    top: Optional[List[Track]] = None
    bottom: Optional[List[Track]] = None
    center: Optional[List[Track]] = None
    whole: Optional[List[Track]] = None
    gallery: Optional[List[Track]] = None

    @validator("*", pre=True)
    def ensure_list(cls, v):
        if v is not None and not isinstance(v, (tuple, list)):
            v = [v]
        return v


Viewconf.update_forward_refs()
View.update_forward_refs()
Tracks.update_forward_refs()
CombinedTrack.update_forward_refs()
DividedTrack.update_forward_refs()
