class ATMCard:
  def __init__(self, default_pin, default_balance):
    self.pin      = default_pin
    self.balance  = default_balance

  def cek_default_pin(self):
    return self.pin

  def cek_default_Balance(self):
    return self.balance