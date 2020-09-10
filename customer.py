from atm_card import ATMCard

class Customer(ATMCard):
  # inisialisasi PIN dan Balance
  # current PIN     = 1234
  # current Balance = Rp10.000
  def __init__(self, cur_Pin=1234, cur_Balance=10000):
    super().__init__(cur_Pin, cur_Balance)

  def cek_pin(self):
    return self.pin

  def cek_balance(self):
    return self.balance

  def debet(self, nominal):
    self.balance = self.balance - nominal
    cur_saldo = self.balance
    return cur_saldo # saldo saat ini setelah di debet
  
  def stor_tunai(self, nominal):
    self.balance = self.balance + nominal
    cur_saldo = self.balance
    return cur_saldo # saldo saat ini setalah ditambah stor tunai :D