from typing import Union, Optional
from dataclasses import dataclass

from oopnet.elements.base import NetworkComponent
from oopnet.elements.system_operation import Pattern, Curve


@dataclass
class Node(NetworkComponent):
    """Base class for all Node like objects in OOPNET (Junction, Reservoir, Tank).

    Attributes:
      xcoordinate: The horizontal location of the junction on the map, measured in the map's distance units. If left blank, the node object will not appear on the network map.
      ycoordinate: The vertical location of the junction on the map, measured in the map's distance units. If left blank, the node object will not appear on the network map.
      elevation: The elevation in meters above some common reference of the node. This is a required property. Elevation is used only to compute pressure at the node. For tanks it is a required property and means Elevation above a common datum in meters of the bottom shell of the tank.
      initialquality: Water quality level at the node at the start of the simulation period. Can be left blank if no water quality analysis is being made or if the level is zero.
      sourcequality: Quality of any water entering the network at this location.
      sourcetype: Source type (CONCEN, MASS, FLOWPACED, or SETPOINT)
      strength: Baseline source strength
      sourcepattern: Time Pattern object of source

    """
    xcoordinate: float = 0.0
    ycoordinate: float = 0.0
    elevation: float = 0.0
    initialquality: float = 0.0
    sourcequality: float = 0.0
    sourcetype: Optional[str] = None
    strength: float = 0.0
    sourcepattern: Optional[list[Pattern]] = None

    @property
    def coordinates(self) -> tuple[float, float, float]:
        """Property returning node coordinates.

        Returns:
            x- and y-coordinate, and elevation

        """
        return self.xcoordinate, self.ycoordinate, self.elevation


@dataclass
class Link(NetworkComponent):
    """Base class for all Link like objects in OOPNET (Pipe, Pump, Valve).

    Attributes:
      startnode: Node-object at the start of the Link
      endnode: Node-object at the end of the Link
      status: Current status of the Link (OPEN, CLOSED, CV or ACTIVE)

    """
    startnode: Optional[Node] = None
    endnode: Optional[Node] = None
    status: str = 'OPEN'

    @property
    def coordinates(self) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        """Property returning start and end node coordinates"""
        return (self.startnode.xcoordinate, self.startnode.ycoordinate, self.startnode.elevation), \
               (self.endnode.xcoordinate, self.endnode.ycoordinate, self.endnode.elevation)

    def revert(self):
        """Switches the link's start and end nodes."""
        self.startnode, self.endnode = self.endnode, self.startnode


@dataclass
class Junction(Node):
    """Defines Junction nodes contained in the network.

    Attributes:
      emittercoefficient: Discharge coefficient for emitter (sprinkler or nozzle) placed at junction. The coefficient represents the flow (in current flow units) that occurs at a pressure drop of 1 meter. Leave blank if no emitter is present. See the Emitters topic in the 'EPANET Manual Section 3.1 <https://epanet22.readthedocs.io/en/latest/3_network_model.html#physical-components>' for more details.
      demandpattern: Pattern object used to characterize time variation in demand for the main category of consumer at the junction. The pattern provides multipliers that are applied to the Base Demand to determine actual demand in a given time period.
      demand: The average or nominal demand for water by the main category of consumer at the junction, as measured in the current flow units. A negative value is used to indicate an external source of flow into the junction.

    """

    emittercoefficient: float = 0.0
    demandpattern: Union[Pattern, list[Pattern], None] = None
    demand: Union[float, list[float]] = 0.0

    @NetworkComponent.id.setter
    def id(self, id: str):
        """Sets ID of NetworkComponent and replaces key in network hash"""
        if self._network:
            self._rename(id=id, hashtable=self._network._nodes['junctions'])
        self._id = id


@dataclass
class Reservoir(Node):
    """Defines all reservoir nodes contained in the network.

    Attributes:
      head: The hydraulic head (elevation + pressure head) of water in the reservoir in meters. This is a required property.
      headpattern: Pattern object used to model time variation in the reservoir's head. Leave blank if none applies. This property is useful if the reservoir represents a tie-in to another system whose pressure varies with time.
      mixingmodel: The type of water quality mixing that occurs within the tank. The choices include MIXED (fully mixed), 2COMP (two-compartment mixing), FIFO (first-in-first-out plug flow) and LIFO (last-in-first-out plug flow).

    """
    head: float = 0.0  # = Either(None, Float, ListFloat)
    headpattern: Optional[Pattern] = None  # = Either(None, Instance(Pattern), List(Instance(Pattern)))

    @NetworkComponent.id.setter
    def id(self, id: str):
        """Sets ID of NetworkComponent and replaces key in network hash"""
        if self._network:
            self._rename(id=id, hashtable=self._network._nodes['reservoirs'])
        self._id = id


@dataclass
class Tank(Node):
    """Defines all tank nodes contained in the network.

    Attributes:
      initlevel: Height in meters of the water surface above the bottom elevation of the tank at the start of the simulation.
      minlevel: Minimum height in meters of the water surface above the bottom elevation that will be maintained. The water level in the tank will not be allowed to drop below this level.
      maxlevel: Maximum height in meters of the water surface above the bottom elevation that will be maintained. The water level in the tank will not be allowed to rise above this level.
      diam: The diameter of the tank in meters. For cylindrical tanks this is the actual diameter. For square or rectangular tanks it can be an equivalent diameter equal to 1.128 times the square root of the cross-sectional area. For tanks whose geometry will be described by a curve (see below) it can be set to any value.
      minvolume: The volume of water in the tank when it is at its minimum level, in cubic meter. This is an optional property, useful mainly for describing the bottom geometry of non-cylindrical tanks where a full volume versus depth curve will not be supplied (see below).
      volumecurve: Curve object used to describe the relation between tank volume and water level. If no value is supplied then the tank is assumed to be cylindrical.
      compartmentvolume: The fraction of the tank’s total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model. Can be left blank if another type of mixing model is employed.
      reactiontank: The bulk reaction coefficient for chemical reactions in the tank. Time units are 1/days. Use a positive value for growth reactions and a negative value for decay. Leave blank if the Global Bulk reaction coefficient specified in the project's Reactions Options will apply. See Water Quality Reactions in the 'EPANETmanual Section 3.4 <https://epanet22.readthedocs.io/en/latest/3_network_model.html#water-quality-simulation-model>' for moreinformation.
      mixingmodel: The type of water quality mixing that occurs within the tank. The choices include MIXED (fully mixed), 2COMP (two-compartment mixing), FIFO (first-in-first-out plug flow) and LIFO (last-in-first-out plug flow).

    """
    initlevel: float = 10.0
    minlevel: float = 0.0
    maxlevel: float = 20.0
    diam: float = 50.0
    minvolume: float = 0.0
    volumecurve: Optional[Curve] = None
    compartmentvolume: Optional[float] = None
    reactiontank: Optional[float] = None
    mixingmodel: str = 'MIXED'  # = Enum('MIXED', '2COMP', 'FIFO', 'LIFO')

    @NetworkComponent.id.setter
    def id(self, id: str):
        """Sets ID of NetworkComponent and replaces key in network hash"""
        if self._network:
            self._rename(id=id, hashtable=self._network._nodes['tanks'])
        self._id = id


@dataclass
class Pipe(Link):
    """Defines all pipe links contained in the network.

    Attributes:
      length: The actual length of the pipe in meters.
      diameter: The pipe diameter in mm.
      roughness: The roughness coefficient of the pipe. It is unitless for Hazen-Williams or Chezy-Manning roughness and has units of mm for Darcy-Weisbach roughness.
      minorloss: Unitless minor loss coefficient associated with bends, fittings, etc. Assumed 0 if left blank.
      reactionbulk: The bulk reaction coefficient for the pipe. Time units are 1/days. Use a positive value for growth and a negative value for decay. Leave blank if the Global Bulk reaction coefficient from the project's Reaction Options will apply. See Water Quality Reactions in the 'EPANET manual Section 3.4<https://epanet22.readthedocs.io/en/latest/3_network_model.html#water-quality-simulation-model>' for moreinformation.
      reactionwall: The wall reaction coefficient for the pipe. Time units are 1/days. Use a positive value for growth and a negative value for decay. Leave blank if the Global Wall reaction coefficient from the project's Reactions Options will apply. See Water Quality Reactions in the 'EPANET manual Section 3.4<https://epanet22.readthedocs.io/en/latest/3_network_model.html#water-quality-simulation-model>' for moreinformation.

    """
    length: float = 1000.0
    diameter: float = 12.0
    roughness: float = 100.0
    minorloss: float = 0.0
    reactionbulk: Optional[float] = None
    reactionwall: Optional[float] = None

    @NetworkComponent.id.setter
    def id(self, id: str):
        """Sets ID of NetworkComponent and replaces key in network hash"""
        if self._network:
            self._rename(id=id, hashtable=self._network._links['pipes'])
        self._id = id


# todo: rethink keyword, value structure (what happens for multiple properties?)
@dataclass
class Pump(Link):
    """Defines all pump links contained in the network.

    todo: implement multiple keyword and value combinations
    Attributes:
      keyword: Can either be POWER (power value for constant energy pump, hp (kW)), HEAD (ID of curve that describeshead versus flow for the pump), SPEED (relative speed setting (normal speed is 1.0, 0 means pump is off)),PATTERN(ID of time pattern that describes how speed setting varies with time). Either POWER or HEAD must be supplied for each pump. The other keywords are optional.
      value: Value according to the keyword attribute
      status: 

    """
    keyword: Optional[str] = None  # = Enum('POWER', 'HEAD', 'SPEED', 'PATTERN')
    value: Union[str, float, None] = None
    setting: Optional[float] = None

    @NetworkComponent.id.setter
    def id(self, id: str):
        """Sets ID of NetworkComponent and replaces key in network hash"""
        if self._network:
            self._rename(id=id, hashtable=self._network._links['pumps'])
        self._id = id


@dataclass
class Valve(Link):
    """Defines all control valve links contained in the network

    Attributes:
      valvetype: A required parameter that describes the valve's operational setting (PRV, PSV, PBV, FCV, TCV, GPV).
      diameter: The valve diameter in mm.
      minorloss: Unitless minor loss coefficient that applies when the valve is completely opened. Assumed 0 if left blank.
      setting: Setting value depending on valvetype.

    """
    diameter: float = 12.0
    minorloss: float = 0.0
    setting: Union[float] = 0.0

    @NetworkComponent.id.setter
    def id(self, id: str):
        """Sets ID of NetworkComponent and replaces key in network hash"""
        if self._network:
            self._rename(id=id, hashtable=self._network._links['valves'])
        self._id = id


@dataclass
class PRV(Valve):
    """Pressure Reducing Valve

     Attributes:
         setting: pressure limit

     """


@dataclass
class TCV(Valve):
    """Throttle Control Valve

     Attributes:
         setting: head loss coefficient

     """


@dataclass
class PSV(Valve):
    """Pressure Sustaining Valve

     Attributes:
         setting: pressure limit at upstream setting

     """


@dataclass
class GPV(Valve):
    """General Purpose Valve

     Attributes:
         setting: Curve representing flow-head loss relationship

     """
    setting: Optional[Curve] = None


@dataclass
class PBV(Valve):
    """Pressure Breaker Valve

     Attributes:
         setting: pressure drop

     """


@dataclass
class FCV(Valve):
    """Flow Control Valve

     Attributes:
         setting: maximum allow flow

     """