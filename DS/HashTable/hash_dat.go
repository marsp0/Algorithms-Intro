package main

// Item - holds the key and the data associated with a single item
type Item struct {
	key  int
	data string
}

// DATable - implements a direct address table.
type DATable struct {
	array []*Item
}

// NewDATable - returns a new DATable with initialized internal structure.
func NewDATable(size int) DATable {
	var initializedArray = make([]*Item, size)
	var value = DATable{array: initializedArray}
	return value
}

// Search - returns the item at index key to the caller.
// O(1)
func (dat *DATable) Search(key int) *Item {
	return dat.array[key]
}

// Insert - inserts an item in the table - O(1)
func (dat *DATable) Insert(item *Item) {
	dat.array[item.key] = item
}

// Delete - deletes an element from the table.
// O(1)
func (dat *DATable) Delete(key int) {
	dat.array[key] = nil
}
