import React from 'react';

const BookItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.id}
            </td>
            <td>
                {item.name}
            </td>
            <td>
                {item.author.name}
            </td>
        </tr>
    )
}

const BookList = ({items}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        ID
                    </th>
                </tr>
                <tr>
                    <th>
                        Name
                    </th>
                </tr>
                <tr>
                    <th>
                        Author
                    </th>
                </tr>
                <tr>
                    {items.map((item) => <BookItem item={item}/>)}
                </tr>
            </thead>
        </table>
    )
}
export default BookList
