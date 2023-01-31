import React from 'react';
import { useParams} from 'react-router-dom';

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
                {item.author.first_name}
            </td>
        </tr>
    )
}

const AuthorBookList = ({items}) => {
    let {id} = useParams()
    let filtered_items = items.filter((item) => item.author.id == id)
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
                    {filtered_items.map((item) => <BookItem item={item} />)}
                </tr>
            </thead>
        </table>
    )
}

export default AuthorBookList
