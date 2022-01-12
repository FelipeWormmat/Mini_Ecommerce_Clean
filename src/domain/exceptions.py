class DiscountExists(Exception):
    public_message = "Já existe um desconto para essa forma de pagamento"


class PaymentMethodDisabled(Exception):
    public_message = "Metodo de pagamento desabilitado"