from abc import ABC, abstractmethod
import functools
import uuid
from datetime import datetime

class Receipt:
    """Generates a receipt for transactions[cite: 1]."""
    def __init__(self, txn_id, amount, method, status):
        self.txn_id = txn_id
        self.amount = amount
        self.method = method
        self.status = status
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Receipt [ID: {self.txn_id}] | Method: {self.method} | Amount: ${self.amount:.2f} | Status: {self.status} | Time: {self.timestamp}"

    def __repr__(self):
        return self.__str__()


class PaymentStrategy(ABC):
    """Abstract base class defining the common interface for all payment methods[cite: 1]."""
    name = "Generic Payment"

    @abstractmethod
    def validate(self):
        """Validates the payment details[cite: 1]."""
        pass

    @abstractmethod
    def pay(self, amount):
        """Processes the payment and returns a Receipt[cite: 1]."""
        pass

    def _make_receipt(self, amount, status):
        """Helper to create a Receipt object[cite: 1]."""
        return Receipt(str(uuid.uuid4()), amount, self.name, status)


class CreditCardPayment(PaymentStrategy):
    name = "Credit Card"

    def __init__(self, card_number, cvv, expiry):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry

    def validate(self):
        return bool(self.card_number and self.cvv and self.expiry)

    def pay(self, amount):
        if self.validate():
            return self._make_receipt(amount, "SUCCESS")
        return self._make_receipt(amount, "FAILED")

class UPIPayment(PaymentStrategy):
    name = "UPI"

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def validate(self):
        return "@" in self.upi_id

    def pay(self, amount):
        if self.validate():
            return self._make_receipt(amount, "SUCCESS")
        return self._make_receipt(amount, "FAILED")

class NetBankingPayment(PaymentStrategy):
    name = "Net Banking"

    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number

    def validate(self):
        return bool(self.bank_name and self.account_number)

    def pay(self, amount):
        if self.validate():
            return self._make_receipt(amount, "SUCCESS")
        return self._make_receipt(amount, "FAILED")

def log_transaction(func):
    """Decorator to log before and after a payment attempt[cite: 1]."""
    @functools.wraps(func)
    def wrapper(self, amount, *args, **kwargs):
        print(f"\n[LOG] Attempting to process payment of ${amount:.2f}...")
        receipt = func(self, amount, *args, **kwargs)
        print(f"[LOG] Transaction finished with status: {receipt.status}")
        return receipt
    return wrapper


class PaymentProcessor:
    """The Context that delegates work to the currently configured strategy[cite: 1]."""

    _registry = {}  # Class attribute mapping key -> strategy class[cite: 1]

    def __init__(self, strategy: PaymentStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Swaps the strategy at run time[cite: 1]."""
        self.strategy = strategy

    @log_transaction
    def process_payment(self, amount):
        """Delegates processing to the active strategy's pay() method[cite: 1]."""
        if not self.strategy:
            raise ValueError("No payment strategy is set.")
        return self.strategy.pay(amount)

    @classmethod
    def register_strategy(cls, key, s_cls):
        """Registers a new strategy to the system[cite: 1]."""
        cls._registry[key] = s_cls

    @classmethod
    def create(cls, key, **kwargs):
        """Factory method to instantiate a processor using a registered strategy name[cite: 1]."""
        s_cls = cls._registry[key]
        return cls(s_cls(**kwargs))

    @classmethod
    def available_methods(cls):
        """Returns a list of registered payment methods[cite: 1]."""
        return list(cls._registry.keys())


def main():
    # Register all four strategies at run time[cite: 1]
    PaymentProcessor.register_strategy("credit_card", CreditCardPayment)
    PaymentProcessor.register_strategy("upi", UPIPayment)
    PaymentProcessor.register_strategy("net_banking", NetBankingPayment)

    while True:
        print("\n" + "="*40)
        print("   INTERACTIVE PAYMENT PROCESSOR")
        print("="*40)

        methods = PaymentProcessor.available_methods()
        print("Available Payment Methods:")
        for idx, method in enumerate(methods, start=1):
            print(f"  {idx}. {method.replace('_', ' ').title()}")
        print(f"  {len(methods) + 1}. Exit")

        choice = input("\nSelect a method (enter number): ").strip()

        # Handle exit
        if choice == str(len(methods) + 1):
            print("Exiting the payment processor. Goodbye!")
            break

        # Handle invalid choice
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(methods):
            print("[ERROR] Invalid choice. Please try again.")
            continue

        selected_method_key = methods[int(choice) - 1]
        kwargs = {}

        print(f"\n--- Enter {selected_method_key.replace('_', ' ').title()} Details ---")

        # Gather dynamic input based on the chosen strategy
        if selected_method_key == "credit_card":
            kwargs["card_number"] = input("Card Number: ")
            kwargs["cvv"] = input("CVV: ")
            kwargs["expiry"] = input("Expiry (MM/YY): ")
        elif selected_method_key == "upi":
            kwargs["upi_id"] = input("UPI ID (must contain '@' to succeed): ")
        elif selected_method_key == "net_banking":
            kwargs["bank_name"] = input("Bank Name: ")
            kwargs["account_number"] = input("Account Number: ")

        # Get transaction amount
        try:
            amount = float(input("\nEnter amount to pay: $"))
        except ValueError:
            print("[ERROR] Invalid amount. Transaction cancelled.")
            continue

        # Instantiate processor using the create() classmethod[cite: 1]
        processor = PaymentProcessor.create(selected_method_key, **kwargs)

        # Process the payment[cite: 1]
        receipt = processor.process_payment(amount)

        # Output the receipt
        print("-" * 40)
        print(receipt)
        print("-" * 40)

        # Loop prompt
        cont = input("\nWould you like to process another transaction? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thank you for using the Payment Processor. Goodbye!")
            break

if __name__ == "__main__":
    main()