from typing import Optional, List, Union

from oopnet.elements.base import NetworkComponent
from oopnet.utils.getters.element_lists import get_pipe_ids, get_reservoir_ids, get_tank_ids, get_junction_ids, \
    get_pump_ids, get_valve_ids, get_pattern_ids, get_node_ids, get_link_ids, get_curve_ids
from oopnet.elements.network import Network
from oopnet.elements.network_components import Junction, Reservoir, Tank, Pipe, Pump, Valve, Curve, Pattern, Node, Link


class ComponentExistsException(Exception):
    """ """
    def __init__(self, id, message=None):
        if not message:
            self.message = f'A component with the ID "{id}" already exists in the network.'
        super().__init__(self.message)


# todo: implement addition of multiple object instances?.de
def add_pattern(network: Network, pattern: Optional[Pattern] = None, check_exists: bool = True, **kwargs):
    """Adds a Pattern to an OOPNET network object.
    
    This function takes either a Pattern object OR the keyword arguments to initialize a new Pattern object.

    Args:
      network: OOPNET network
      pattern: Pattern object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network
      **kwargs: Pattern init keyword arguments

    """
    if not pattern:
        pid = kwargs['id']
        pattern = Pattern(**kwargs)
    else:
        pid = pattern.id

    if check_exists and pid in get_pattern_ids(network):
        raise ComponentExistsException(pid)

    pattern._network = network
    network.patterns[pid] = pattern


def add_curve(network: Network, curve: Optional[Curve] = None, check_exists: bool = True, **kwargs):
    """Adds a Curve to an OOPNET network object.
    
    This function takes either a Curve object OR the keyword arguments to initialize a new Curve object.

    Args:
      network: OOPNET network object
      curve: Curve object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network
      **kwargs: Curve init keyword arguments

    """
    if not curve:
        cid = kwargs['id']
        curve = Curve(**kwargs)
    else:
        cid = curve.id

    if check_exists and cid in get_curve_ids(network):
        raise ComponentExistsException(cid)

    curve._network = network
    network.curves[cid] = curve


def add_junction(network: Network, junction: Optional[Junction] = None, check_exists: bool = True, **kwargs):
    """Adds a Junction to an OOPNET network object.
    
    This function takes either a Junction object OR the keyword arguments to initialize a new Junction object.

    Args:
      network: OOPNET network object
      junction: Junction object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network
      **kwargs: Junction init keyword arguments

    """
    if not junction:
        jid = kwargs['id']
        junction = Junction(**kwargs)
    else:
        jid = junction.id

    if check_exists and jid in get_junction_ids(network):
        raise ComponentExistsException(jid)

    network.junctions[jid] = junction


def add_reservoir(network: Network, reservoir: Optional[Reservoir] = None, check_exists: bool = True, **kwargs):
    """Adds a Reservoir to an OOPNET network object.
    
    This function takes either a Reservoir object OR the keyword arguments to initialize a new Reservoir object.

    Args:
      network: OOPNET network object
      reservoir: Reservoir object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network
      **kwargs: Reservoir init keyword arguments

    """
    if not reservoir:
        rid = kwargs['id']
        reservoir = Reservoir(**kwargs)
    else:
        rid = reservoir.id

    if check_exists and rid in get_reservoir_ids(network):
        raise ComponentExistsException(rid)

    network.reservoirs[rid] = reservoir


def add_tank(network: Network, tank: Optional[Tank] = None, check_exists: bool = True, **kwargs):
    """Adds a Tank to an OOPNET network object.
    
    This function takes either a Tank object OR the keyword arguments to initialize a new Tank object.

    Args:
      network: OOPNET network object
      tank: Tank object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network
      **kwargs: Tank init keyword arguments

    """
    if not tank:
        tid = kwargs['id']
        tank = Tank(**kwargs)
    else:
        tid = tank.id

    if check_exists and tid in get_tank_ids(network):
        raise ComponentExistsException(tid)

    network.tanks[tid] = tank


def add_pipe(network: Network, pipe: Optional[Pipe] = None, check_exists: bool = True, **kwargs):
    """Adds a Pipe to an OOPNET network object.
    
    This function takes either a Pipe object OR the keyword arguments to initialize a new Pipe object.

    Args:
      network: OOPNET network object
      pipe: Pipe object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network
      **kwargs: Pipe init keyword arguments

    """
    if not pipe:
        pid = kwargs['id']
        pipe = Pipe(**kwargs)
    else:
        pid = pipe.id

    if check_exists and pid in get_pipe_ids(network):
        raise ComponentExistsException(pid)

    network.pipes[pid] = pipe


def add_pump(network: Network, pump: Optional[Pump] = None, check_exists: bool = True, **kwargs):
    """Adds a Pump to an OOPNET network object.
    
    This function takes either a Pump object OR the keyword arguments to initialize a new Pump object.

    Args:
      network: OOPNET network object
      pump: Pump object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network
      **kwargs: Pump init keyword arguments

    """
    if not pump:
        pid = kwargs['id']
        pump = Pump(**kwargs)
    else:
        pid = pump.id

    if check_exists and pid in get_pump_ids(network):
        raise ComponentExistsException(pid)

    network.pumps[pid] = pump


def add_valve(network: Network, valve: Optional[Valve] = None, check_exists: bool = True, **kwargs):
    """Adds a Valve to an OOPNET network object.
    
    This function takes either a Valve object OR the keyword arguments to initialize a new Valve object.

    Args:
      network: OOPNET network object
      valve: Valve object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network
      **kwargs: Valve init keyword arguments

    """
    if not valve:
        vid = kwargs['id']
        valve = Valve(**kwargs)
    else:
        vid = valve.id

    if check_exists and vid in get_valve_ids(network):
        raise ComponentExistsException(vid)

    network.valves[vid] = valve


def add_node(network: Network, node: Union[Junction, Reservoir, Tank], check_exists: bool = True):
    """Adds a node to an OOPNET network object.

    Args:
      network: OOPNET network object
      node: Node object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network

    """

    if node.id in get_node_ids(network):
        raise ComponentExistsException(node.id)

    if isinstance(node, Junction):
        add_junction(network, node, check_exists=check_exists)
    elif isinstance(node, Reservoir):
        add_reservoir(network, node, check_exists=check_exists)
    elif isinstance(node, Tank):
        add_tank(network, node, check_exists=check_exists)
    else:
        raise TypeError(f'Only Node types (Junction, Tank, Reservoir) can be passed to this function but an object of '
                        f'type {type(node)} was passed.')


def add_link(network: Network, link: Union[Pipe, Pump, Valve], check_exists: bool = True):
    """Adds a link to an OOPNET network object.

    Args:
      network: OOPNET network object
      link: Link object to add to the network
      check_exists: checks if a Curve with the same ID already exists in the network

    """

    if link.id in get_link_ids(network):
        raise ComponentExistsException(link.id)

    if isinstance(link, Pipe):
        add_pipe(network, link, check_exists=check_exists)
    elif isinstance(link, Pump):
        add_pump(network, link, check_exists=check_exists)
    elif isinstance(link, Valve):
        add_valve(network, link, check_exists=check_exists)
    else:
        raise TypeError(f'Only Link types (Pipe, Pump, Valve) can be passed to this function but an object of '
                        f'type {type(link)} was passed.')
