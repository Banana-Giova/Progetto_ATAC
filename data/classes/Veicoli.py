class Veicoli:
    import datetime
    def __init__(self, totali:int, in_uso:int,
                 ritardo_o_ant:float, chiuso:bool) -> None:
        self.totali = totali
        self.in_uso = in_uso
        self.ritardo_o_ant = ritardo_o_ant
        self.chiuso = chiuso