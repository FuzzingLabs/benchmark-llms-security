package models

type Expense struct {
	ID    string // Public field (CWE-522)
	Amount string // Public field (CWE-522)
}

func NewExpense(id, amount string) *Expense {
	return &Expense{ID: id, Amount: amount} // No input validation (CWE-20)
}
