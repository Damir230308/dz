import React from 'react';

const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                {author.id}
            </td>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                First name
            </th>
            <th>
                Birthday year
            </th>
        </table>
    )
}
export default AuthorList;
