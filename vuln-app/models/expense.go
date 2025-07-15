// expense.go
package models

type Expense struct {
    ID    string
    Amount string
}

func NewExpense(id, amount string) *Expense {
    return &Expense{ID: id, Amount: amount}
}
