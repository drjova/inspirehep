import getValue from '../../common/getValue';

export const countryOptions = [
  { value: 'Afghanistan' },
  { value: 'Åland Islands' },
  { value: 'Albania' },
  { value: 'Algeria' },
  { value: 'American Samoa' },
  { value: 'Andorra' },
  { value: 'Angola' },
  { value: 'Anguilla' },
  { value: 'Antarctica' },
  { value: 'Antigua and Barbuda' },
  { value: 'Argentina' },
  { value: 'Armenia' },
  { value: 'Aruba' },
  { value: 'Australia' },
  { value: 'Austria' },
  { value: 'Azerbaijan' },
  { value: 'Bahamas' },
  { value: 'Bahrain' },
  { value: 'Bangladesh' },
  { value: 'Barbados' },
  { value: 'Belarus' },
  { value: 'Belgium' },
  { value: 'Belize' },
  { value: 'Benin' },
  { value: 'Bermuda' },
  { value: 'Bhutan' },
  { value: 'Bolivia' },
  { value: 'Bosnia and Herzegovina' },
  { value: 'Botswana' },
  { value: 'Bouvet Island' },
  { value: 'Brazil' },
  { value: 'British Indian Ocean Territory' },
  { value: 'Brunei Darussalam' },
  { value: 'Bulgaria' },
  { value: 'Burkina Faso' },
  { value: 'Burundi' },
  { value: 'Cambodia' },
  { value: 'Cameroon' },
  { value: 'Canada' },
  { value: 'Cape Verde' },
  { value: 'Cayman Islands' },
  { value: 'Central African Republic' },
  { value: 'Chad' },
  { value: 'Chile' },
  { value: 'China' },
  { value: 'Christmas Island' },
  { value: 'Cocos (Keeling) Islands' },
  { value: 'Colombia' },
  { value: 'Comoros' },
  { value: 'Congo' },
  { value: 'Congo, The Democratic Republic of the' },
  { value: 'Cook Islands' },
  { value: 'Costa Rica' },
  { value: "Cote D'Ivoire" },
  { value: 'Croatia' },
  { value: 'Cuba' },
  { value: 'Cyprus' },
  { value: 'Czech Republic' },
  { value: 'Denmark' },
  { value: 'Djibouti' },
  { value: 'Dominica' },
  { value: 'Dominican Republic' },
  { value: 'Ecuador' },
  { value: 'Egypt' },
  { value: 'El Salvador' },
  { value: 'Equatorial Guinea' },
  { value: 'Eritrea' },
  { value: 'Estonia' },
  { value: 'Ethiopia' },
  { value: 'Falkland Islands (Malvinas' },
  { value: 'Faroe Islands' },
  { value: 'Fiji' },
  { value: 'Finland' },
  { value: 'France' },
  { value: 'French Guiana' },
  { value: 'French Polynesia' },
  { value: 'French Southern Territories' },
  { value: 'Gabon' },
  { value: 'Gambia' },
  { value: 'Georgia' },
  { value: 'Germany' },
  { value: 'Ghana' },
  { value: 'Gibraltar' },
  { value: 'Greece' },
  { value: 'Greenland' },
  { value: 'Grenada' },
  { value: 'Guadeloupe' },
  { value: 'Guam' },
  { value: 'Guatemala' },
  { value: 'Guernsey' },
  { value: 'Guinea' },
  { value: 'Guinea-Bissau' },
  { value: 'Guyana' },
  { value: 'Haiti' },
  { value: 'Heard Island and Mcdonald Islands' },
  { value: 'Holy See (Vatican City State' },
  { value: 'Honduras' },
  { value: 'Hong Kong' },
  { value: 'Hungary' },
  { value: 'Iceland' },
  { value: 'India' },
  { value: 'Indonesia' },
  { value: 'Iran, Islamic Republic Of' },
  { value: 'Iraq' },
  { value: 'Ireland' },
  { value: 'Isle of Man' },
  { value: 'Israel' },
  { value: 'Italy' },
  { value: 'Jamaica' },
  { value: 'Japan' },
  { value: 'Jersey' },
  { value: 'Jordan' },
  { value: 'Kazakhstan' },
  { value: 'Kenya' },
  { value: 'Kiribati' },
  { value: "Korea, Democratic People'S Republic of" },
  { value: 'Korea, Republic of' },
  { value: 'Kuwait' },
  { value: 'Kyrgyzstan' },
  { value: "Lao People'S Democratic Republic" },
  { value: 'Latvia' },
  { value: 'Lebanon' },
  { value: 'Lesotho' },
  { value: 'Liberia' },
  { value: 'Libyan Arab Jamahiriya' },
  { value: 'Liechtenstein' },
  { value: 'Lithuania' },
  { value: 'Luxembourg' },
  { value: 'Macao' },
  { value: 'Macedonia, The Former Yugoslav Republic of' },
  { value: 'Madagascar' },
  { value: 'Malawi' },
  { value: 'Malaysia' },
  { value: 'Maldives' },
  { value: 'Mali' },
  { value: 'Malta' },
  { value: 'Marshall Islands' },
  { value: 'Martinique' },
  { value: 'Mauritania' },
  { value: 'Mauritius' },
  { value: 'Mayotte' },
  { value: 'Mexico' },
  { value: 'Micronesia, Federated States of' },
  { value: 'Moldova, Republic of' },
  { value: 'Monaco' },
  { value: 'Mongolia' },
  { value: 'Montserrat' },
  { value: 'Morocco' },
  { value: 'Mozambique' },
  { value: 'Myanmar' },
  { value: 'Namibia' },
  { value: 'Nauru' },
  { value: 'Nepal' },
  { value: 'Netherlands' },
  { value: 'Netherlands Antilles' },
  { value: 'New Caledonia' },
  { value: 'New Zealand' },
  { value: 'Nicaragua' },
  { value: 'Niger' },
  { value: 'Nigeria' },
  { value: 'Niue' },
  { value: 'Norfolk Island' },
  { value: 'Northern Mariana Islands' },
  { value: 'Norway' },
  { value: 'Oman' },
  { value: 'Pakistan' },
  { value: 'Palau' },
  { value: 'Palestinian Territory, Occupied' },
  { value: 'Panama' },
  { value: 'Papua New Guinea' },
  { value: 'Paraguay' },
  { value: 'Peru' },
  { value: 'Philippines' },
  { value: 'Pitcairn' },
  { value: 'Poland' },
  { value: 'Portugal' },
  { value: 'Puerto Rico' },
  { value: 'Qatar' },
  { value: 'Reunion' },
  { value: 'Romania' },
  { value: 'Russian Federation' },
  { value: 'RWANDA' },
  { value: 'Saint Helena' },
  { value: 'Saint Kitts and Nevis' },
  { value: 'Saint Lucia' },
  { value: 'Saint Pierre and Miquelon' },
  { value: 'Saint Vincent and the Grenadines' },
  { value: 'Samoa' },
  { value: 'San Marino' },
  { value: 'Sao Tome and Principe' },
  { value: 'Saudi Arabia' },
  { value: 'Senegal' },
  { value: 'Serbia and Montenegro' },
  { value: 'Seychelles' },
  { value: 'Sierra Leone' },
  { value: 'Singapore' },
  { value: 'Slovakia' },
  { value: 'Slovenia' },
  { value: 'Solomon Islands' },
  { value: 'Somalia' },
  { value: 'South Africa' },
  { value: 'South Georgia and the South Sandwich Islands' },
  { value: 'Spain' },
  { value: 'Sri Lanka' },
  { value: 'Sudan' },
  { value: 'Surivalue' },
  { value: 'Svalbard and Jan Mayen' },
  { value: 'Swaziland' },
  { value: 'Sweden' },
  { value: 'Switzerland' },
  { value: 'Syrian Arab Republic' },
  { value: 'Taiwan, Province of China' },
  { value: 'Tajikistan' },
  { value: 'Tanzania, United Republic of' },
  { value: 'Thailand' },
  { value: 'Timor-Leste' },
  { value: 'Togo' },
  { value: 'Tokelau' },
  { value: 'Tonga' },
  { value: 'Trinidad and Tobago' },
  { value: 'Tunisia' },
  { value: 'Turkey' },
  { value: 'Turkmenistan' },
  { value: 'Turks and Caicos Islands' },
  { value: 'Tuvalu' },
  { value: 'Uganda' },
  { value: 'Ukraine' },
  { value: 'United Arab Emirates' },
  { value: 'United Kingdom' },
  { value: 'United States' },
  { value: 'United States Minor Outlying Islands' },
  { value: 'Uruguay' },
  { value: 'Uzbekistan' },
  { value: 'Vanuatu' },
  { value: 'Venezuela' },
  { value: 'Viet Nam' },
  { value: 'Virgin Islands, British' },
  { value: 'Virgin Islands, U.S' },
  { value: 'Wallis and Futuna' },
  { value: 'Western Sahara' },
  { value: 'Yemen' },
  { value: 'Zambia' },
  { value: 'Zimbabwe' },
];
export const countryValues = countryOptions.map(getValue);