from .decorators import section_writer


@section_writer('TITLE', 0)
def write_title(network, fid):
    print('[TITLE]', file=fid)
    if network.title is not None:
        print(network.title, file=fid)
    print('\n', file=fid)


@section_writer('JUNCTIONS', 1)
def write_junctions(network, fid):
    print('[JUNCTIONS]', file=fid)
    print(';id elevation demand demandpattern', file=fid)
    if network.junctions is not None:
        for j in network.junctions:
            print(j.id, end=' ', file=fid)
            if j.elevation is not None:
                print(j.elevation, end=' ', file=fid)
            if j.demand is not None:
                if isinstance(j.demand, list):
                    print(j.demand[0], end=' ', file=fid)
                else:
                    print(j.demand, end=' ', file=fid)
            if j.demandpattern is not None:
                if isinstance(j.demandpattern, list):
                    print(j.demandpattern[0].id, end=' ', file=fid)
                else:
                    print(j.demandpattern.id, end=' ', file=fid)
            if j.comment is not None:
                print(';', j.comment, end=' ', file=fid)
            print('\n', end=' ', file=fid)
    print('\n', end=' ', file=fid)


@section_writer('RESERVOIRS', 1)
def write_reservoirs(network, fid):
    print('[RESERVOIRS]', file=fid)
    print(';id head pattern', file=fid)
    if network.reservoirs is not None:
        for r in network.reservoirs:
            print(r.id, end=' ', file=fid)
            if r.head is not None:
                print(r.head, end=' ', file=fid)
            if r.headpattern is not None:
                print(r.headpattern.id, end=' ', file=fid)
            if r.comment is not None:
                print(';', r.comment, end=' ', file=fid)
            print('\n', end=' ', file=fid)
    print('\n', end=' ', file=fid)


@section_writer('TANKS', 1)
def write_tanks(network, fid):
    print('[TANKS]', file=fid)
    print(';id elevation initlevel minlevel maxlevel diam minvolume volumecurve', file=fid)
    if network.tanks is not None:
        for t in network.tanks:
            print(t.id, end=' ', file=fid)
            if t.elevation is not None:
                print(t.elevation, end=' ', file=fid)
            if t.initlevel is not None:
                print(t.initlevel, end=' ', file=fid)
            if t.minlevel is not None:
                print(t.minlevel, end=' ', file=fid)
            if t.maxlevel is not None:
                print(t.maxlevel, end=' ', file=fid)
            if t.diam is not None:
                print(t.diam, end=' ', file=fid)
            if t.minvolume is not None:
                print(t.minvolume, end=' ', file=fid)
            if t.volumecurve is not None:
                print(t.volumecurve, end=' ', file=fid)
            if t.comment is not None:
                print(';', t.comment, end=' ', file=fid)
            print('\n', end=' ', file=fid)
    print('\n', end=' ', file=fid)


@section_writer('PIPES', 2)
def write_pipes(network, fid):
    print('[PIPES]', file=fid)
    print(';id startnode endnode length diameter roughness minorloss status', file=fid)
    if network.pipes is not None:
        for p in network.pipes:
            print(p.id, end=' ', file=fid)
            if p.startnode is not None:
                print(p.startnode.id, end=' ', file=fid)
            if p.endnode is not None:
                print(p.endnode.id, end=' ', file=fid)
            if p.length is not None:
                print(p.length, end=' ', file=fid)
            if p.diameter is not None:
                print(p.diameter, end=' ', file=fid)
            if p.roughness is not None:
                print(p.roughness, end=' ', file=fid)
            if p.minorloss is not None:
                print(p.minorloss, end=' ', file=fid)
            if p.status is not None:
                print(p.status, end=' ', file=fid)
            if p.comment is not None:
                print(';', p.comment, end=' ', file=fid)
            print('\n', end=' ', file=fid)
    print('\n', end=' ', file=fid)


@section_writer('PUMPS', 2)
def write_pumps(network, fid):
    print('[PUMPS]', file=fid)
    print(';id startnode endnode keyword value', file=fid)
    if network.pumps is not None:
        for p in network.pumps:
            print(p.id, end=' ', file=fid)
            if p.startnode is not None:
                print(p.startnode.id, end=' ', file=fid)
            if p.endnode is not None:
                print(p.endnode.id, end=' ', file=fid)
            if p.keyword is not None:
                print(p.keyword, end=' ', file=fid)
            if p.value is not None:
                print(p.value, end=' ', file=fid)
            if p.comment is not None:
                print(';', p.comment, end=' ', file=fid)
            print('\n', end=' ', file=fid)
    print('\n', end=' ', file=fid)


@section_writer('VALVES', 2)
def write_valves(network, fid):
    print('[VALVES]', file=fid)
    print(';id startnode endnode diameter valvetype setting minorloss', file=fid)
    if network.valves is not None:
        for v in network.valves:
            print(v.id, end=' ', file=fid)
            if v.startnode is not None:
                print(v.startnode.id, end=' ', file=fid)
            if v.endnode is not None:
                print(v.endnode.id, end=' ', file=fid)
            if v.diameter is not None:
                print(v.diameter, end=' ', file=fid)
            if v.valvetype is not None:
                print(v.valvetype, end=' ', file=fid)
            if v.setting is not None:
                print(v.setting, end=' ', file=fid)
            if v.minorloss is not None:
                print(v.minorloss, end=' ', file=fid)
            if v.comment is not None:
                print(';', v.comment, end=' ', file=fid)
            print('\n', end=' ', file=fid)
    print('\n', end=' ', file=fid)


@section_writer('EMITTERS', 3)
def write_emitter(network, fid):
    print('[EMITTERS]', file=fid)
    print(';id emittercoefficient', file=fid)
    if network.junctions is not None:
        for j in network.junctions:
            if j.emittercoefficient > 0.0:
                print(j.id, j.emittercoefficient, file=fid)
    print('\n', file=fid)
